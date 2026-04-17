"""
class purposed with the create, read, update, and delete functions of a hand of cards
"""

from collections import deque
from typing import Deque, Set, Tuple

from poker_python_project.app.card import Card
from poker_python_project.app.deck import Deck
from poker_python_project.app.score import Score


class Hand:
    """
    A Players collection of cards that have been dealt to them
    """

    def __init__(self, draw_from: Deck) -> None:
        """
        Hand must have a Deck to draw from
        """
        self._deck = draw_from
        self._cards: Deque[Card] = deque()
        self._search: Set[Card] = set()
        self._score: Score

    def check(self, card: Card) -> bool:
        """
        Check if the named card is in hand
        """
        return card in self._search

    def discard(self, card: Card) -> None:
        """
        Take a named card from hand and add to the discard pile
        """
        if self.check(card):
            self._cards.remove(card)
            self._search.remove(card)
            self._deck.discarded.extend([card])

    def draw(self, number: int) -> Deque[Card]:
        """
        Take cards from the Deck and add them to hand
        """
        cards_drawn: Deque[Card] = self._deck.draw(number)
        self._cards.extend(cards_drawn)
        self._search.update(cards_drawn)
        return cards_drawn

    def show(self) -> Deque[Card]:
        """
        Return the list of cards in hand
        """
        return self._cards

    def play(self, card: Card, removed: bool = True) -> Card | None:
        """
        Return a card from Hand, and optionally discard afterwards
        """
        if self.check(card):
            if removed:
                self.discard(card)
            return card
        return None

    def score(self) -> Tuple[int, int, str]:
        """
        Calculate the score for the hand based on the game_rules
        """
        self._score = Score(self._cards)
        return self._score.calculate()
