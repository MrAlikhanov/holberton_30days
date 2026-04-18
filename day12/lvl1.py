# Day 11 - Functions - Level 3

import re

# 1. Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(2))   # True
print(is_prime(7))   # True
print(is_prime(10))  # False

# 2. Check if all items are unique
def is_unique(lst):
    return len(lst) == len(set(lst))

print(is_unique([1, 2, 3, 4]))      # True
print(is_unique([1, 2, 2, 4]))      # False

# 3. Check if all items are the same data type
def is_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
    return True

print(is_same_type([1, 2, 3]))         # True
print(is_same_type([1, 'two', 3]))     # False
print(is_same_type(['a', 'b', 'c']))   # True

# 4. Check if a variable name is a valid Python variable
def is_valid_variable(name):
    # must start with letter or underscore, followed by letters, digits or underscores
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    # also must not be a Python keyword
    keywords = [
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
        'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
        'while', 'with', 'yield'
    ]
    if name in keywords:
        return False
    return bool(re.match(pattern, name))

print(is_valid_variable('first_name'))  #
