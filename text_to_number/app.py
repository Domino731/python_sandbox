import string

# APP: 01
# DATE: 19.02.2023
# Description: create an app that will receive string and print index of each string letter

def letters_indexes(text):
    payload = ''

    for letter in text:
        try:
            payload += str(string.ascii_lowercase.index(letter.lower()))
        except:
            payload += letter

    return payload


input_payload = input('What text do you want to convert to numbers')
payload = letters_indexes(input_payload)

print('Output: ', payload)

assert letters_indexes('ABCD') == '0123'
assert letters_indexes('My name is John') == '1224 130124 818 914713'