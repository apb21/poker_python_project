from dataclasses import dataclass

@dataclass(frozen=True)
class Card:
    name: str
    suit: str
    value: str
    symbol: str
