# APP: 07
# DATE: 22.02.2023
# Description: create a simple rock, paper, scissors game
import random

ROCK_NAME = 'rock'
PAPER_NAME = 'paper'
SCISSORS_NAME = 'scissors'

# tuple structure - 1 - can be defeated by..., 2 - can win against...
DATA = {
    ROCK_NAME: (PAPER_NAME, SCISSORS_NAME),
    PAPER_NAME: (SCISSORS_NAME, ROCK_NAME),
    SCISSORS_NAME: (ROCK_NAME, PAPER_NAME)
}


def get_random_item():
    return random.choice(list(DATA.items()))


def check_result(computer, user):
    user_choice = DATA.get(user)
    if computer == user:
        return None
    else:
        return computer == user_choice[1]


is_winning = False
score = 0
while is_winning:
    computer_choice = get_random_item()
    computer_item_name = computer_choice[0]
    computer_item_props = computer_choice[1]
    user_choice = ''
    while user_choice not in DATA.keys():
        user_choice = input('Enter rock, paper or scissors: ')

    result = check_result(computer_item_name, user_choice)
    print('Computer choice is ' + computer_item_name)
    print('Your choice is ' + user_choice)

    if result is None:
        print('Draw!')
    elif result:
        score += 1
    else:
        is_winning = False

print('Game over, your score is ' + str(score))
