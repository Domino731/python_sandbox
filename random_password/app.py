import random
import string

# APP: 07
# DATE: 23.02.2023
# Description: create an app for generating password


password_length = 20
specials = 3
strings = 0
numbers = 0

specials_characters = ['!', '@', '#', '$', '%', '^', '&', '/', '(', '*']

# set strings and numbers amount
strings = random.randint(0, password_length - specials)
numbers = password_length - (specials + strings)


def get_strings():
    data = []
    for i in range(strings):
        data.append(random.choice(string.ascii_letters))

    return data


def get_numbers():
    data = []
    for i in range(numbers):
        data.append(random.randint(0, 9))
    return data


def get_specials():
    data = []
    for i in range(specials):
        data.append(random.choice(specials_characters))
    return data


def shuffle_string(string):
    l = list(string)
    random.shuffle(l)
    result = ''.join(l)
    return result


def create_password():
    password = ''
    for i in get_strings():
        password += i
    for i in get_numbers():
        password += str(i)
    for i in get_specials():
        password += i

    return shuffle_string(password)


print('Generated password: ' + create_password())
