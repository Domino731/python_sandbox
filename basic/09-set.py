names_set = {"Kamil", "Adam", "Kamil"}
print(names_set)

name_set_2 = set()
name_set_2.add('Kamil')
name_set_2.add('Adam')
name_set_2.add('Kamil')
name_set_2.add('John')
name_set_2.add(('1', '2'))

# you can't add mutable data to set (list, dict)
# name_set_2.add([1,2,3])

for name in name_set_2:
    print(name)

name_set_2.discard('Kamil')

# merge 2 sets
name_set_3 = name_set_2.union(names_set)

# update new set 2
name_set_2.update(names_set)

differences = name_set_2.difference(names_set)
intersection = name_set_2.intersection(names_set)