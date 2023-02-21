from dice_rolling.dices import DICES
import random

# APP: 04
# DATE: 20.02.2023
# Description: create an app/game responsible for generating specific amount of dices

DICES_AMOUNT = len(DICES.values())


def print_dice(index):
    if DICES_AMOUNT >= index > 0:
        for dice_line in DICES.get(index):
            print(dice_line)


print(type(DICES.get(1)))

while True:
    try:
        dices = int(input('How many throws of the dice do you want?, type 0 to exit'))
        if dices == 0:
            break
        for i in range(0, dices):
            print_dice(random.randint(1, DICES_AMOUNT))
    except ValueError:
        print('Invalid number')

assert DICES_AMOUNT == 6
assert all(type(dice) is tuple for dice in DICES.values()) == True
