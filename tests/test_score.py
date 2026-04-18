"""
run a series of test on the app/score.py file to ensure it is working
"""

from collections import Counter, deque
from unittest.mock import MagicMock, patch

import pytest

from poker_python_project.app.score import Score

# Mock data to simulate game.json structure
MOCK_SCORE_RULES = {
    "card_scores": {
        "2": [2],
        "3": [3],
        "4": [4],
        "5": [5],
        "6": [6],
        "7": [7],
        "8": [8],
        "9": [9],
        "10": [10],
        "J": [11],
        "Q": [12],
        "K": [13],
        "A": [1, 14],
    },
    "hand_ranks": {
        "high_card": {
            "rank_value": 1,
            "value_count": 5,
            "value_max": 1,
            "suit_count": 4,
            "max_range": 13,
            "min_value": 1,
        },
        "pair": {
            "rank_value": 2,
            "value_count": 4,
            "value_max": 2,
            "suit_count": 4,
            "max_range": 13,
            "min_value": 1,
        },
        "flush": {
            "rank_value": 6,
            "value_count": 5,
            "value_max": 1,
            "suit_count": 1,
            "max_range": 13,
            "min_value": 1,
        },
    },
}


@pytest.fixture
def _mock_card():
    """Helper to create mock card objects."""

    def _create_card(value, suit, symbol):
        card = MagicMock()
        card.value = value
        card.suit = suit
        card.symbol = symbol
        return card

    return _create_card


@pytest.fixture
def _score_instance():
    """Fixture to initialize Score with mocked file resources."""
    with patch("importlib.resources.files") as mock_res:
        # Mocking the file reading boilerplate in __post_init__
        mock_path = mock_res.return_value.join_path.return_value
        mock_context = mock_path.open.return_value
        mock_file = MagicMock()
        mock_context.__enter__.return_value = mock_file

        with patch("json.load", return_value=MOCK_SCORE_RULES):
            yield Score


def test_calculate_high_card(_score_instance, _mock_card):
    """Test identifying a basic High Card hand."""
    hand = deque(
        [
            _mock_card("2", "H", "2H"),
            _mock_card("4", "D", "4D"),
            _mock_card("7", "S", "7S"),
            _mock_card("9", "C", "9C"),
            _mock_card("A", "H", "AH"),  # This is the high card
        ]
    )

    scorer = _score_instance(hand=hand)
    rank_val, high_val, name = scorer.calculate()

    assert rank_val == 1
    assert high_val == 14
    assert "high_card" in name
    assert "AH" in name


def test_calculate_pair(_score_instance, _mock_card):
    """Test identifying a Pair."""
    hand = deque(
        [
            _mock_card("10", "H", "10H"),
            _mock_card("10", "D", "10D"),  # Pair of 10s
            _mock_card("3", "S", "3S"),
            _mock_card("5", "C", "5C"),
            _mock_card("7", "H", "7H"),
        ]
    )

    scorer = _score_instance(hand=hand)
    rank_val, high_val, name = scorer.calculate()

    assert rank_val == 2
    assert high_val == 10
    assert "pair" in name


def test_calculate_flush(_score_instance, _mock_card):
    """Test identifying a Flush (all same suit)."""
    hand = deque(
        [
            _mock_card("2", "H", "2H"),
            _mock_card("5", "H", "5H"),
            _mock_card("8", "H", "8H"),
            _mock_card("J", "H", "JH"),
            _mock_card("K", "H", "KH"),
        ]
    )

    scorer = _score_instance(hand=hand)
    rank_val, high_val, name = scorer.calculate()

    assert rank_val == 6
    assert high_val == 13
    assert "flush" in name
    assert "KH" in name


def test_post_init_loads_data(_score_instance):
    """Verify that _score_rules is populated on initialization."""
    scorer = _score_instance(hand=deque())
    assert scorer.score_rules == MOCK_SCORE_RULES


def test_matrix_approach(_score_instance, _mock_card):
    """
    Test if you can discover the hand layout using a matrix-style approach
    """
    # mock hand with a pair of 10s
    hand = deque(
        [
            _mock_card("10", "H", "10H"),
            _mock_card("10", "D", "10D"),  # Pair of 10s
            _mock_card("3", "S", "3S"),
            _mock_card("5", "C", "5C"),
            _mock_card("7", "H", "7H"),
        ]
    )
    # pull current scorer to get access to the score_rules
    scorer = _score_instance(hand=hand)
    # Build a matrix of the values in the hand
    hand_coords = {
        (scorer.score_rules["card_scores"][card.value][0], card.suit) for card in hand
    }
    # Count the matrix in each direction to understand the layout
    row_counts = Counter(r for r, s in hand_coords)
    col_counts = Counter(s for r, s in hand_coords)
    # Sort the rows to understand the most common card values
    significant_rows = sorted(
        row_counts.items(), key=lambda x: (x[1], x[0]), reverse=True
    )
    # Get the most common value from the top corner of the matrix
    top_value_idx = significant_rows[0][0]
    # Match the top value across the matrix to get the suits with that value
    suit_of_top_value = [s for r, s in hand_coords if r == top_value_idx]

    # assert your discoveries
    assert "D" in suit_of_top_value  # one of each
    assert "H" in suit_of_top_value  # one of each
    assert max(col_counts.values()) == 2  # pair
    assert significant_rows[0] == (10, 2)  # pair of 10's
