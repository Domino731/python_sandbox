from rock_paper_scissors.app import DATA, get_random_item, check_result, ROCK_NAME, PAPER_NAME, SCISSORS_NAME

assert len(DATA.values()) == 3
assert type(get_random_item()) is tuple
assert type(get_random_item()[1]) is tuple
assert get_random_item()[0] in DATA.keys()

# checking check_result function - checking none
assert check_result(ROCK_NAME, ROCK_NAME) is None
assert check_result(PAPER_NAME, PAPER_NAME) is None
assert check_result(SCISSORS_NAME, SCISSORS_NAME) is None

# checking check_result function - checking real results
assert check_result(ROCK_NAME, SCISSORS_NAME) == False
assert check_result(ROCK_NAME, PAPER_NAME) == True
assert check_result(PAPER_NAME, ROCK_NAME) == False
assert check_result(PAPER_NAME, SCISSORS_NAME) == True
assert check_result(SCISSORS_NAME, ROCK_NAME) == True
assert check_result(SCISSORS_NAME, PAPER_NAME) == False

