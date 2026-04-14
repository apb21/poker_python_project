"""
run a series of test on the app/deck.py file to ensure it is working
"""

from poker_python_project.app.deck import Deck


def test_deck_creation_works():
    """
    Ensure deck creation returns a deque
    """
    test_deck = Deck(True)
    assert isinstance(test_deck, Deck)


def test_deck_creation_shuffle():
    """
    test an unshuffled deck matches an unshuffled deck
    and doesn't match a shuffled deck
    """
    straight_deck = Deck(False)
    shuffled_deck1 = Deck(True)
    shuffled_deck2 = Deck(True)
    test_deck = Deck(False)
    assert (
        test_deck.remaining == straight_deck.remaining
        and test_deck.remaining != shuffled_deck1.remaining
        and test_deck.remaining != shuffled_deck2.remaining
        and shuffled_deck1.remaining != shuffled_deck2.remaining
    )


def test_draw_function():
    """
    Test the draw function returns the right number of cards
    """
    test_deck = Deck(True)
    test_hand = test_deck.draw(3)
    assert len(test_hand) == 3


def test_symbols_shown():
    """
    Test correct symbols are shown for cards
    """
    test_card = "ace of spades"
    test_deck = Deck(True)
    test_symbol = test_deck.symbols[test_card]
    assert test_symbol == "A♠️"


def test_deck_taken_equals_hand():
    """
    test that the cards in hand match cards taken
    """
    test_deck = Deck(True)
    test_hand = test_deck.draw(5)
    assert test_hand == test_deck.taken


def test_taken_and_remaining_is_total():
    """
    taken and remaining should be all cards after draw
    """
    test_deck = Deck(True)
    test_deck.draw(7)
    assert set(test_deck.remaining + test_deck.taken).issubset(test_deck.cards)


def test_mill_discards_cards():
    """
    milled cards should end up in the discard pile
    """
    test_deck = Deck(True)
    discarded_cards = test_deck.mill(10)
    assert test_deck.discarded == discarded_cards and not set(
        test_deck.discarded
    ).issubset(test_deck.remaining)
