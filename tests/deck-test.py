"""
run a series of test on the app/deck.py file to ensure it is working
use "python -m tests.deck-test" to run
"""

from app.deck import Deck

print("Create Test Deck")
test_deck = Deck(True)

print("Draw 3 cards")
test_hand = test_deck.draw(3)
print(f"Cards Drawn: {test_hand}")

print("Show symbols for hand")
for test_card in test_hand:
    print(test_deck.symbols[test_card])

print("Show card that have been taken")
print(test_deck.taken)

print("Show cards remaining")
print(test_deck.remaining)

print("Draw 3 more cards")
test_hand2 = test_deck.draw(3)
print(f"Cards Drawn: {test_hand2}")

print("Show card that have been taken")
print(test_deck.taken)

print("Mill 10 cards")
milled_cards = test_deck.mill(10)
print(f"Milled Cards: {milled_cards}")

print("Show Discarded Cards")
print(test_deck.discarded)

print("Discard test_hand cards")
test_deck.discarded.extend(test_hand)
test_hand.clear()
print(f"Cards in test_hand: {test_hand}")
print(f"Cards in test_hand2: {test_hand2}")

print("Show Discarded Cards")
print(test_deck.discarded)

print("Recycle Discarded Cards")
test_deck.recycle(True)

print("Show Discarded Cards")
print(test_deck.discarded)

print("Show card that have been taken")
print(test_deck.taken)
print(f"Cards in test_hand2: {test_hand2}")

print("Show cards remaining")
print(test_deck.remaining)
