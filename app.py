import os
import random

# Amount of chips player has
starting_chips = 1000
total_chips = starting_chips


# Sorting out JQK + A's
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


# The cards in the deck
while True:
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', ] * 4

# Randomises/shuffling cards
    random.shuffle(deck)

# Player 1 + computer
    dealer = []
    player = []

# Dealing cards
    player.append(deck.pop())
    dealer.append(deck.pop())
    player.append(deck.pop())
    dealer.append(deck.pop())

# Stating first deal (important for blackjack)
    first_hand = True

# Player yet too stick
    sticking = False


    while True:
        os.system('cls' if os.name == 'nt' else 'clear')



        print('Player 1 has {}\n'.format(total_chips))

        # Amount of chips player wants to bet
        try:
            placed_bet = int(input('Place your bet: '))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        print('')

        if placed_bet > total_chips:
            print("You don't have enough funds")
            continue
        else:
            break

    print('You now have: {}\n'.format(total_chips - placed_bet))

    # If player wins

    while True:
    # Value of player + computers hands
            player_score = calc_hand(player)
            dealer_score = calc_hand(dealer)

            if sticking:
                print('Dealer Cards: [{}] ({})'.format(']['.join(dealer), dealer_score))
    # Hiding dealers second card
            else:
                print('Dealer Cards: [{}][?]'.format(dealer[0]))
    # Showing both players cards
            print('Your Cards:   [{}] ({})\n'.format(']['.join(player), player_score))

    # Game outcomes
            if sticking:
                if dealer_score > 21:
                    total_chips = (total_chips - placed_bet)
                    total_chips = ((placed_bet * 2) + total_chips)
                    print('Dealer busted, you win!\n')
                    print('You now have: {}'.format(total_chips))
                elif player_score == dealer_score:
                    total_chips = (total_chips - placed_bet)
                    print('Draw, no winner!')
                    print('You now have: {}'.format(total_chips))
                elif player_score > dealer_score:
                    total_chips = (total_chips - placed_bet)
                    total_chips = ((placed_bet * 2) + total_chips)
                    print('You beat the dealer, you win!')
                    print('You now have: {}'.format(total_chips))
                else:
                    total_chips = (total_chips - placed_bet)
                    print('You lose\n')
                    print('You now have: {}\n'.format(total_chips))
                input('Play again? Hit enter to continue')
                break

            if first_hand and player_score == 21:
                total_chips = (total_chips - placed_bet)
                total_chips = ((placed_bet * 2) + total_chips)
                print('Blackjack!\n')
                print('You now have: {}\n'.format(total_chips))
                input('Play again? Hit enter to continue')
                break

            if player_score > 21:
                total_chips = (total_chips - placed_bet)
                print('You bust!\n')
                print('You now have: {}\n'.format(total_chips))
                input('Play again? Hit enter to continue')
                break

    # Option to stick or twist
            print('What would you like to do?')
            print(' [1] Stick')
            print(' [2] Twist\n')
            choice = input('Your choice: ')

    # Showing it's not players first hand
            first_hand = False

    # Sticking if input = 1
            if choice == '1':
                sticking = True

    # Keep going until dealer gets <= 15
                while calc_hand(dealer) <= 15:
                    dealer.append(deck.pop())

    # Or twist again if input = 2
            elif choice == '2':
                player.append(deck.pop())