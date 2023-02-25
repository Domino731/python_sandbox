from random_password.app import create_password, get_numbers, get_specials, get_strings, specials_characters, shuffle_string

assert type(get_numbers()) is list
assert type(get_strings()) is list
assert type(get_specials()) is list
assert type(get_numbers()[0]) is int
assert type(get_strings()[0]) is str
assert type(get_specials()[0]) is str
assert type(create_password()) is str
assert type(specials_characters) is list
assert type(shuffle_string('lorem_ipsum_999')) is str
assert shuffle_string('lorem_ipsum_999') is not 'lorem_ipsum_999'