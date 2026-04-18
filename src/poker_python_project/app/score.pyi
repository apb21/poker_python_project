from dataclasses import dataclass
from poker_python_project.app.card import Card as Card
from typing import Deque

@dataclass
class Score:
    hand: Deque[Card]
    def __post_init__(self) -> None: ...
    def calculate(self) -> tuple[int, int, str]: ...
