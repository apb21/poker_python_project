"""
class purposed with create, read, update, delete functions of a deck (deque) of cards
"""

import json
import random
from collections import deque
from importlib import resources
from itertools import islice
from typing import Deque

from poker_python_project.app.card import Card


class Deck:
    """
    Build a deck of cards
    """

    def __init__(self, shuffled: bool = True) -> None:
        """
        create a list of cards loaded from data/deck.json
        """
        cards: Deque[Card] = deque()
        remaining: Deque[Card] = deque()
        taken: Deque[Card] = deque()
        discarded: Deque[Card] = deque()
        source = resources.files("poker_python_project.data").joinpath("deck.json")
        with source.open("r", encoding="utf-8") as file:
            data = json.load(file)
            for suit in data["suit_names"]:
                for card in data["card_names"]:
                    this_card = Card(
                        name=f"{card} of {suit}",
                        suit=suit,
                        value=card,
                        symbol=(
                            str(data["card_symbols"][card])
                            + str(data["suit_symbols"][suit])
                        ),
                    )
                    cards.append(this_card)
                    remaining.append(this_card)
            if shuffled:
                temp_list = list(remaining)
                random.shuffle(temp_list)
                remaining = deque(temp_list)
            # The list of cards in the deck overall
            self.cards: Deque = cards
            # The cards still remaining in the deck (initally all of them)
            self.remaining: Deque = remaining
            # The cards taken from the deck (initially none of them)
            self.taken: Deque = taken
            # The cards taken from the deck and then discarded (not in hand)
            self.discarded: Deque = discarded

    def draw(self, number: int = 1) -> Deque[Card]:
        """
        remove cards from the "top" of the remaining cards and record they are taken.
        """
        drawn: Deque[Card] = deque(islice(self.remaining, number))
        for _ in range(len(drawn)):
            self.remaining.popleft()
        self.taken.extend(drawn)
        return drawn

    def mill(self, number: int = 1) -> Deque[Card]:
        """
        move cards from the top of the deck to the discard pile
        """
        milled: Deque[Card] = deque(islice(self.remaining, number))
        for _ in range(len(milled)):
            self.remaining.popleft()
        self.discarded.extend(milled)
        return milled

    def peek(self, number: int = 1) -> Deque[Card]:
        """
        reveal cards from the "top" of the deck without removing them (in same order)
        """
        peeked: Deque[Card] = deque(islice(self.remaining, number))
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
        self.taken = deque(card for card in self.taken if card not in recycled_set)
        self.discarded.clear()
        completed = True
        return completed
