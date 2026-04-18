# Day 11 - Functions - Level 2

import math

# 1. Evens and odds counter
def evens_and_odds(n):
    odds = 0
    evens = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")

evens_and_odds(100)

# 2. Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))   # 120
print(factorial(10))  # 3628800

# 3. Is empty
def is_empty(value):
    if value == 0:
        return False
    return not bool(value)

print(is_empty([]))        # True
print(is_empty(''))        # True
print(is_empty({}))        # True
print(is_empty([1, 2, 3])) # False
print(is_empty('hello'))   # False

# 4. Statistical functions
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    return sorted_lst[mid]

def calculate_mode(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    max_count = max(frequency.values())
    mode = [k for k, v in frequency.items() if v == max_count]
    return mode

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))

data = [2, 4, 4, 4, 5, 5, 7, 9]
print("Mean:", calculate_mean(data))        # 5.0
print("Median:", calculate_median(data))    # 4.5
print("Mode:", calculate_mode(data))        # [4]
print("Range:", calculate_range(data))      # 7
print("Variance:", calculate_variance(data))# 4.0
print("Std Dev:", calculate_std(data))      # 2.0

# 5. Greet with default argument
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Hello, Guest!
greet("Alice")   # Hello, Alice!

# 6. Show arbitrary named arguments
def show_args(**kwargs):
    args_str = ", ".join(f"{k}: {v}" for k, v in kwargs.items())
    print(f"Received: {args_str}")

show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")
