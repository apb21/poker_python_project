"""
class purposed with create, read, update, delete functions of a deck (deque) of cards
"""

import typing
import json
import random
from collections import deque
from itertools import islice


class Deck:
    def __init__(self, shuffled: bool = True) -> None:
        """
        create a list of cards loaded from data/deck.json
        """
        cards: deque[str] = deque()
        remaining: deque[str] = deque()
        taken: deque[str] = deque()
        discarded: deque[str] = deque()
        symbols: dict[str, str] = {}
        with open("data/deck.json", "r") as file:
            data = json.load(file)
            for suit in data["suit_names"]:
                for card in data["card_names"]:
                    this_card = f"{card} of {suit}"
                    this_symbol = (
                        f"{data["card_symbols"][card]}{data["suit_symbols"][suit]}"
                    )
                    cards.append(this_card)
                    remaining.append(this_card)
                    symbols[this_card] = this_symbol
            if shuffled:
                temp_list = list(remaining)
                random.shuffle(temp_list)
                remaining = deque(temp_list)
            # The list of cards in the deck overall
            self.cards = cards
            # The symbols for the cards in the deck
            self.symbols = symbols
            # The cards still remaining in the deck (initally all of them)
            self.remaining = remaining
            # The cards taken from the deck (initially none of them)
            self.taken = taken
            # The cards taken from the deck and then discarded (not in hand), initally none of them
            self.discarded = discarded

    def draw(self, number: int = 1) -> deque[str]:
        """
        remove cards from the "top" of the remaining cards and record that they are taken.
        """
        drawn: deque[str] = deque(islice(self.remaining, number))
        for _ in range(len(drawn)):
            self.remaining.popleft()
        self.taken.extend(drawn)
        return drawn

    def mill(self, number: int = 1) -> deque[str]:
        """
        move cards from the top of the deck to the discard pile
        """
        milled: deque[str] = deque(islice(self.remaining, number))
        for _ in range(len(milled)):
            self.remaining.popleft()
        self.discarded.extend(milled)
        return milled

    def peek(self, number: int = 1) -> deque[str]:
        """
        reveal cards from the "top" of the deck without removing them (remain in same order)
        """
        peeked: deque[str] = deque(islice(self.remaining, number))
        return peeked

    def recycle(self, shuffled: bool = True) -> bool:
        """
        recycle the discarded cards back in to the remaining cards
        """
        completed = False
        self.remaining.extend(self.discarded)
        if shuffled:
            temp_list = list(self.remaining)
            random.shuffle(temp_list)
            self.remaining = deque(temp_list)
        recycled_set: set[str] = set(self.discarded)
        self.taken: deque[str] = deque(
            card for card in self.taken if card not in recycled_set
        )
        self.discarded.clear()
        completed = True
        return completed
