"""
class for holding the data structure for the score of a Hand
"""

import json
from collections import Counter
from dataclasses import dataclass
from importlib import resources
from typing import Deque, Tuple

from poker_python_project.app.card import Card


@dataclass
class Score:
    """
    Calculates the score for a given Hand.
    """

    hand: Deque[Card]
    _rank_value: Tuple[int, int, str] = (0, 0, "Not Calculated")

    def __post_init__(self) -> None:
        source = resources.files("poker_python_project.data").joinpath("game.json")
        with source.open("r", encoding="utf-8") as file:
            data = json.load(file)
            self._score_rules = data

    def calculate(self) -> Tuple[int, int, str]:
        """
        Compare the Hand to the score_rules to get a rank.
        Returns a Tuple of [
            max_rank: 1 to 10,
            high_card: 1 to 14,
            rank_str: "{rank_name} high card:{card_symbol}"
        ]
        Higher numbers of max_rank and high_card are better.
        """
        value_counter = Counter(card.value for card in self.hand)
        value_count = len(value_counter)
        value_max = max(value_counter.values())
        high_card = max(
            max(self._score_rules["card_scores"][val]) for val in value_counter.keys()
        )
        min_value = min(
            min(self._score_rules["card_scores"][val]) for val in value_counter.keys()
        )
        max_range = high_card - min_value
        suit_counter = Counter(card.suit for card in self.hand)
        suit_count = len(suit_counter)
        max_rank = max(
            (
                rank["rank_value"]
                for rank in self._score_rules["hand_ranks"].values()
                if value_count == rank["value_count"]
                and value_max == rank["value_max"]
                and suit_count <= rank["suit_count"]
                and max_range <= rank["max_range"]
                and min_value >= rank["min_value"]
            ),
            default=1,
        )
        max_rank_name = next(
            (
                name
                for name, rank in self._score_rules["hand_ranks"].items()
                if rank["rank_value"] == max_rank
            ),
            "Unknown",
        )
        best_card = max(
            self.hand,
            key=lambda x: max(self._score_rules["card_scores"].get(x.value, 0)),
        )
        best_card_symbol = best_card.symbol
        rank_name = f"{str(max_rank_name)} (with high card {str(best_card_symbol)})"
        self._rank_value = (int(max_rank), int(high_card), rank_name)
        return self._rank_value

    @property
    def score_rules(self):
        """
        Get the underlying score rules for the score
        """
        return self._score_rules
