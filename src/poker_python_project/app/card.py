"""
Immutable dataclass holding details about an individual card.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    """
    Individual Card object
    """

    name: str
    suit: str
    value: str
    symbol: str

    def __str__(self) -> str:
        """
        Str method for using print on Card
        """
        return self.name

    def __repr__(self) -> str:
        """
        Represent the card as its symbol when printing a Deck or Hand
        """
        return self.symbol
