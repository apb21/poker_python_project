"""
class purposed with create, read, update, delete functions of a deck of cards
"""

import typing
import json
import random


class Deck:
    def __init__(self, shuffled: boolean):
        """
        create a list of cards loaded from data/deck.json
        """
        cards = []
        remaining = []
        taken = []
        symbols = {}
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
                random.shuffle(remaining)
            # The list of cards in the deck overall
            self.cards = cards
            # The symbols for the cards int he deck
            self.symbols = symbols
            # The cards still remaining in the deck (initally all of them)
            self.remaining = remaining
            # The cards take from the deck (initially none of them)
            self.taken = taken

    def draw(self, number: int = 1) -> List:
        """
        remove cards from the "top" of the remaining cards and record that they are taken.
        """
        drawn = []
        while number > 0:
            if len(self.remaining) > 0:
                drawn_card = self.remaining.pop(0)
                drawn.append(drawn_card)
                self.taken.append(drawn_card)
            number = number - 1
        return drawn
