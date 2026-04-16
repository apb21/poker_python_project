"""
run a series of test on the app/card.py file to ensure it is working
"""

from dataclasses import FrozenInstanceError

import pytest

from poker_python_project.app.card import Card


def test_card_initialization():
    """Verify that a card stores attributes correctly."""
    card = Card(name="Ace of Spades", suit="Spades", value="14", symbol="A♠")
    assert card.name == "Ace of Spades"
    assert card.suit == "Spades"
    assert card.value == "14"
    assert card.symbol == "A♠"


def test_card_str_method():
    """Verify __str__ returns only the name (for print calls)."""
    card = Card(name="King of Hearts", suit="Hearts", value="13", symbol="K♥")
    assert str(card) == "King of Hearts"


def test_card_repr_method():
    """Verify __repr__ returns only the symbol (for deque/list display)."""
    card = Card(name="Queen of Diamonds", suit="Diamonds", value="12", symbol="Q♦")
    assert repr(card) == "Q♦"


def test_card_immutability():
    """Confirm that the card is frozen and cannot be modified."""
    card = Card(name="Ten of Clubs", suit="Clubs", value="10", symbol="10♣")
    with pytest.raises(FrozenInstanceError):
        card.name = "New Name"
    with pytest.raises(FrozenInstanceError):
        card.value = "11"


def test_card_equality():
    """Dataclasses provide __eq__ by default; verify it works."""
    card1 = Card(name="Jack", suit="Spades", value="11", symbol="J♠")
    card2 = Card(name="Jack", suit="Spades", value="11", symbol="J♠")
    card3 = Card(name="Ace", suit="Hearts", value="14", symbol="A♥")

    assert card1 == card2  # Should be equal because data is identical
    assert card1 != card3  # Should not be equal
