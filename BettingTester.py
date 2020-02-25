# Amount of chips player has
available_to_bet = list(range(1, 1001))

# Need to change so that you can lose + gain chips
amount_of_chips = 1000


print('Player 1 has {}\n'.format(amount_of_chips))


# Amount of chips player wants to bet
placed_bet = int(input('Place your bet: '))

print('')

if placed_bet > 1000:
    print("You don't have enough funds")
elif placed_bet < 1000:
    print('You have bet {}'.format(placed_bet))

# A deduction from players total chips of the total bet
print('You now have: {}\n'.format(amount_of_chips - placed_bet))

# If win double that money

# Else total stays at what was deducted