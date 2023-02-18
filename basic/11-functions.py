countries_and_capitals = {'Poland': 'Warsaw', 'Germany': 'Berlin', 'USA': 'Washington DC', 'France': 'Paris'}

index = 0
print('Which country capital do you want to display?')
for country in countries_and_capitals:
    index += 1
    print(str(index) + ' ' + country)


def display_country_capital(country):
    if country in countries_and_capitals:
        capital = countries_and_capitals.get(country)
        print('The capital of ' + country + ' is ' + capital)
    else:
        print('Country not found in database')


correct_country = False
selected_country = ''


while not correct_country:
    selected_country = input('Choose the country from list: ')
    if selected_country in countries_and_capitals:
        correct_country = True
    else:
        print('Chose a valid country')

display_country_capital(selected_country)
