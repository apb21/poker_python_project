"""
run a series of test on the app/deck.py file to ensure it is working
"""

from app.deck import Deck

test_deck = Deck(True)

test_hand = test_deck.draw(3)

print(test_hand)

for test_card in test_hand:
    print(test_deck.symbols[test_card])

print(test_deck.taken)

print(test_deck.remaining)

test_hand2 = test_deck.draw(3)

print(test_hand2)

print(test_deck.taken)
