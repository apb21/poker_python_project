"""
main code for running poker_python_project
"""

from poker_python_project.app.deck import Deck
from poker_python_project.app.hand import Hand


def main():
    """
    Do some stuff with the poker_python_project
    """
    print("Hello from poker-python-project!")
    new_deck = Deck(True)
    hand = Hand(new_deck)
    drawn_cards = hand.draw(5)
    print(f"You've drawn: {drawn_cards}")
    for card in hand.show():
        print(card)
    hand_score = hand.score()
    print(hand_score[2])


if __name__ == "__main__":
    main()
