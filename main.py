"""
main code for running poker_python_project
"""

from poker_python_project.app.deck import Deck


def main():
    """
    Do some stuff with the poker_python_project
    """
    print("Hello from poker-python-project!")
    new_deck = Deck(True)
    hand = new_deck.draw(3)
    print(hand)
    for card in hand:
        print(new_deck.symbols[card])


if __name__ == "__main__":
    main()
