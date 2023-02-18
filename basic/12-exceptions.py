countries_and_capitals = {'USA': 'Washington DC'}

try:
    print(2 / 0)
    print(countries_and_capitals['France'])
except KeyError:
    print('A KeyError occurred because countries_and_capitols does not holding data about france')
except ZeroDivisionError:
    print('A ZeroDivisionError occurred because you cant divide 2 by 0')
finally:
    print('Success')