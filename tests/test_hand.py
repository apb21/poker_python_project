"""
run a series of test on the app/hand.py file to ensure it is working
"""

from collections import Counter, deque

from poker_python_project.app.hand import Deck, Hand


def test_starts_empty():
    """
    The initial show of the hand should be an empty deque
    """
    test_deck = Deck(True)
    test_hand = Hand(test_deck)

    assert test_hand.show() == deque()


def test_draw_and_show_length_match():
    """
    Test drawing X cards returns a deque of X cards
    """
    test_deck = Deck(True)
    test_hand = Hand(test_deck)
    draw_length = 7
    drawn_cards = test_hand.draw(draw_length)

    assert draw_length == len(drawn_cards) == len(test_hand.show())


def test_draw_and_show_match():
    """
    Test drawing X cards returns the same cards as show()
    """
    test_deck = Deck(True)
    test_hand = Hand(test_deck)
    drawn_cards = test_hand.draw(7)

    assert Counter(drawn_cards) == Counter(test_hand.show())


def test_play_returns_one():
    """
    Test play() returns one card
    """
    test_deck = Deck(True)
    test_hand = Hand(test_deck)
    test_hand.draw(7)
    first_card = test_hand.show()[0]
    play_one = test_hand.play(first_card)

    assert 1 == len([play_one])


def test_discard_matches_discarded():
    """
    Test discarded cards are in the discard pile of the deck
    """
    test_deck = Deck(True)
    test_hand = Hand(test_deck)
    drawn_cards = test_hand.draw(7)
    first_card = drawn_cards[0]
    test_hand.discard(first_card)

    assert deque([first_card]) == test_deck.discarded


def test_play_matches_discarded():
    """
    Test played cards are in the discard pile of the deck
    """
    test_deck = Deck(True)
    test_hand = Hand(test_deck)
    drawn_cards = test_hand.draw(7)
    first_card = drawn_cards[0]
    played_card = test_hand.play(first_card, True)

    assert deque([first_card]) == deque([played_card]) == test_deck.discarded


def test_draw_all_cards():
    """
    Test drawing LARGE numbers of cards is all (52) cards from the deck
    """
    test_deck = Deck(True)
    test_hand = Hand(test_deck)
    draw_length = 10000
    drawn_cards = test_hand.draw(draw_length)

    assert (
        draw_length != len(drawn_cards) == len(test_hand.show()) == len(test_deck.cards)
    )
