name = 'Carol'
# length
print(len(name))
# first letter will be capitalized
print(name.capitalize())
# all letters will be capitalized
print(name.upper())
# get letter on specific index
print(name[0])
# get letter in specific range
print(name[0:2])
# check if string starts with ...
print(name.startswith('C'))
# check if string ends with ...
print(name.endswith('l'))
# remove last letter from right
print(name.rstrip('l'))
# remove last letter from right
print(name.lstrip('C'))
# remove all letters from string
print(name.strip('a'))
# strip() method is also removing all unnecessary spaces
print('   Carol'.strip())
# convert number to string
print(str(7).zfill(3))

name = 'How to learn python'

# split to words
print(name.split(' '))

# join specific word in list
join_string = '-'
print(join_string.join(['How', 'to', 'learn', 'python']))