a = 1
b = 2

if a == 1 or b == 2:
    print('Or operator has worked well')

if a == 12:
    print('a variable is equal to 12')
elif b == 2:
    print('b variable is equal to 2')

signal = 'Red'

print('Go') if signal != 'Red' else print('Stop')
