"""
class purposed with the create, read, update, and delete functions of a hand of cards
"""

from collections import deque

from poker_python_project.app.deck import Deck


class Hand:
    """
    A Players collection of cards that have been dealt to them
    """

    def __init__(self, draw_from: Deck) -> None:
        """
        Hand must have a Deck to draw from
        """
        self._deck = draw_from
        self._cards: deque[str] = deque()
        self._search: set[str] = set()

    def check(self, card: str) -> bool:
        """
        Check if the named card is in hand
        """
        return card in self._search

    def discard(self, card: str) -> None:
        """
        Take a named card from hand and add to the discard pile
        """
        if self.check(card):
            self._cards.remove(card)
            self._search.remove(card)
            self._deck.discarded.extend([card])

    def draw(self, number: int) -> deque[str]:
        """
        Take cards from the Deck and add them to hand
        """
        cards_drawn = self._deck.draw(number)
        self._cards.extend(cards_drawn)
        self._search.update(cards_drawn)
        return cards_drawn

    def show(self) -> deque[str]:
        """
        Return the list of cards in hand
        """
        return self._cards

    def play(self, card: str, removed: bool = True) -> str | None:
        """
        Return a card from Hand, and optionally discard afterwards
        """
        if self.check(card):
            if removed:
                self.discard(card)
            return card
        return None
