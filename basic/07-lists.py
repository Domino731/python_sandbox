# In python we have lists which are one of complex data types, python list === javascript array
names = ['John', 'Adam']

print(names)
print(names[0])

programming_languages = ['c++', 'python', 'javaScript', 'c#', 'javaScript']

# add "c" to list
programming_languages.append('c')

# simple example how to go through the array by using for loop
for lang in programming_languages:
    print('programming language', lang)

# reverse list
print(programming_languages.reverse())
# sort list
print(programming_languages.sort())
# return number of keyword in array
print(programming_languages.count('javaScript'))
# return list length
print(len(programming_languages))
# make list empty
programming_languages.clear()
print(programming_languages)

# merge both arrays
new_array = names + programming_languages
new_array.sort(reverse=True)
print(new_array)
