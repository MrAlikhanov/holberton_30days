# Day 14 - Higher Order Functions - Level 1

from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1. Difference between map, filter and reduce
"""
map()    - applies a function to EVERY item in a list and returns a new list
filter() - keeps only items where the function returns True
reduce() - combines all items into a SINGLE value using the function
"""

# map example - square every number
squared = list(map(lambda x: x**2, numbers))
print("map:", squared)      # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filter example - keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("filter:", evens)     # [2, 4, 6, 8, 10]

# reduce example - sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print("reduce:", total)     # 55


# 2. Higher order function, closure and decorator
"""
Higher order function - a function that takes another function as argument
                        or returns a function as result.

Closure              - an inner function that remembers variables from its
                        enclosing scope even after the outer function has finished.

Decorator            - a function that wraps another function to add extra
                        behaviour without changing the original function.
"""

# Higher order function example
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 2, 5))   # 10

# Closure example
def multiplier(factor):
    def multiply(number):
        return number * factor      # remembers 'factor' from outer scope
    return multiply

double = multiplier(2)
triple = multiplier(3)
print(double(5))    # 10
print(triple(5))    # 15

# Decorator example
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return 'hello world'

print(greet())  # HELLO WORLD


# 3. Call function before map, filter, reduce

def square(x):
    return x ** 2

def is_even(x):
    return x % 2 == 0

def add(x, y):
    return x + y

print(list(map(square, numbers)))           # [1, 4, 9, ...]
print(list(filter(is_even, numbers)))       # [2, 4, 6, 8, 10]
print(reduce(add, numbers))                 # 55


# 4. Print each country
for country in countries:
    print(country)

# 5. Print each name
for name in names:
    print(name)

# 6. Print each number
for number in numbers:
    print(number)
