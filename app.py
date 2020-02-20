import os
import random

def calc_hand(hand):
    non_aces = [c for c in hand if c != 'A']
    aces = [c for c in hand if c == 'A']

    sum = 0

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

while True:
    deck = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',]*4

    random.shuffle(deck)

    dealer = []
    player = []

    player.append(deck.pop())
    dealer.append(deck.pop())
    player.append(deck.pop())
    dealer.append(deck.pop())

    first_hand = True
    sticking = False

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        player_score = calc_hand(player)
        dealer_score = calc_hand(dealer)

        if sticking:
            print('Dealer Cards: [{}] ({})'.format(']['.join(dealer), dealer_score))
        else:
            print('Dealer Cards: [{}][?]'.format(dealer[0]))

        print('Your Cards:   [{}] ({})'.format(']['.join(player), player_score))
        print('')

        if sticking:
            if dealer_score > 21:
                print('Dealer busted, you win!')
            elif player_score == dealer_score:
                print('Draw, no winner!')
            elif player_score > dealer_score:
                print('You beat the dealer, you win!')
            else:
                print('You lose\n')
            input('Play again? Hit enter to continue')
            break

        if first_hand and player_score == 21:
            print('Blackjack!\n')
            input('Play again? Hit enter to continue')
            break

        if player_score > 21:
            print('You bust!\n')
            input('Play again? Hit enter to continue')
            break

        print('What would you like to do?')
        print(' [1] Stick')
        print(' [2] Twist\n')
        choice = input('Your choice: ')


        first_hand = False

        if choice == '1':
            sticking = True
            while calc_hand(dealer) <= 16:
                dealer.append(deck.pop())
        elif choice == '2':
            player.append(deck.pop())