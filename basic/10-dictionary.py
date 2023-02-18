countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}
countries_and_capitals["France"] = "Paris"

print(countries_and_capitals)

# use for to display keys
for country in countries_and_capitals.keys():
    print(country)

# use for to display values
for capital in countries_and_capitals.values():
    print(capital)

# use for to display key and value
for country, capital in countries_and_capitals.items():
    print(country + ' - ' + capital)

# check if key exists in dictionary if not the set passed value
countries_and_capitals.setdefault('Poland', 'Krakow')
countries_and_capitals.setdefault('USA', 'Washington DC')

# how to get value from dict?
# 1. be aware that the key must exists with this approach
print(countries_and_capitals['Poland'])
# 2. key does not have to be in dictionary
print(countries_and_capitals.get('Spain'))

# checking if key exists
if 'Poland' in countries_and_capitals:
    print('Poland exists!!!!')
else:
    print('Not found :(')

# remove key
countries_and_capitals.pop('Poland')

# remove last added value to the dictionary
countries_and_capitals.popitem()