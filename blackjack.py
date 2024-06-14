card_deck = [4,11,8,5,13,2,10]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())

    print(hand)