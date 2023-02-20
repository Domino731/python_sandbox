import math
from os import system, name
import random

# APP: 02
# DATE: 20.02.2023
# Description: create an app/game for guessing the random number, user can enter min and max value and
# amount of available mistakes. After reaching maximum mistakes the game ends

min_number = 0
max_number = 0
available_mistakes = -1
current_mistakes = 0
user_score = 0
invalid_input_text = 'Enter a valid number'


def generate_random_number(min, max):
    return random.randint(min, max)


while available_mistakes <= -1:
    try:
        available_mistakes = math.ceil(float(input('Enter available mistakes: ')))
    except:
        print(invalid_input_text)

while min_number <= 0:
    try:
        min_number = math.ceil(float(input('Enter min number: ')))
    except:
        print(invalid_input_text)

while max_number <= min_number:
    try:
        max_number = math.ceil(float(input('Enter max number: ')))
    except:
        print(invalid_input_text)

user_number = -1
target_number = -1

while current_mistakes <= available_mistakes:
    if target_number == -1:
        target_number = generate_random_number(min_number, max_number)

    user_number = math.ceil(float(input('Enter number: ')))

    if user_number == target_number:
        user_score += 1
        target_number = generate_random_number(min_number, max_number)
        print('Congrats, you guessed the number!')
    else:
        current_mistakes += 1

