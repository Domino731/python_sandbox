import string

# APP: 01
# DATE: 19.02.2023
# Description: create an app that will receive string and print index of each string letter

text = input('What text do you want to convert to numbers')

payload = ''

for letter in text:
    payload += str(string.ascii_lowercase.index(letter.lower()))

print('Output: ', payload)
