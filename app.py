import random
import os
# hand total
def calc_hand(hand):
    sum = 0

#
    non_aces = [deck for deck in hand if deck != 'A']
    aces = [deck for deck in hand if deck != 'A']

    for deck in non_aces:
        if deck in 'JQK':
            sum += 10
        else:
            sum += int(deck)

    for deck in aces:
        if sum <= 10:
            sum += 11
        else:
            sum += 1

    return sum

# deck
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', ]*4

random.shuffle(deck)

# dealer
dealer = []

# player
player = []

# draw a card
player.append(deck.pop())
dealer.append(deck.pop())
player.append(deck.pop())
dealer.append(deck.pop())

# clears screen
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    player_score = calc_hand(player)
    dealer_score = calc_hand(dealer)

    print('Dealer Cards: [{}][?]'.format(dealer[0]))
    print('Your Cards [{}] ({})'.format(']['.join(player), player_score))

    break