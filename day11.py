# Day 11 - Functions - Level 1

import math

# 1. Add two numbers
def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(3, 5))  # 8

# 2. Area of a circle
def area_of_circle(r):
    return math.pi * r * r

print(area_of_circle(5))  # 78.53...

# 3. Sum arbitrary number of arguments
def add_all_nums(*args):
    for num in args:
        if not isinstance(num, (int, float)):
            return "All arguments must be numbers!"
    return sum(args)

print(add_all_nums(1, 2, 3, 4))       # 10
print(add_all_nums(1, 2, 'a', 4))     # error message

# 4. Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(convert_celsius_to_fahrenheit(100))  # 212.0
print(convert_celsius_to_fahrenheit(0))    # 32.0

# 5. Check season
def check_season(month):
    month = month.capitalize()
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Invalid month'

print(check_season('December'))  # Winter
print(check_season('April'))     # Spring

# 6. Calculate slope
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(2, 2, 6, 10))  # 2.0

# 7. Solve quadratic equation ax² + bx + c = 0
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return 'No real solutions'

print(solve_quadratic_eqn(1, -3, 2))   # (2.0, 1.0)
print(solve_quadratic_eqn(1, 2, 1))    # -1.0
print(solve_quadratic_eqn(1, 1, 1))    # No real solutions

# 8. Print list items
def print_list(lst):
    for item in lst:
        print(item)

print_list([1, 2, 3])

# 9. Reverse a list using loop
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print(reverse_list([1, 2, 3, 4, 5]))    # [5, 4, 3, 2, 1]
print(reverse_list(['A', 'B', 'C']))    # ['C', 'B', 'A']

# 10. Capitalize list items
def capitalize_list_items(lst):
    capitalized = []
    for item in lst:
        capitalized.append(item.capitalize())
    return capitalized

print(capitalize_list_items(['python', 'django', 'flask']))  # ['Python', 'Django', 'Flask']

# 11. Add item to list
def add_item(lst, item):
    lst.append(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))   # ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))           # [2, 3, 7, 9, 5]

# 12. Remove item from list
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))           # [2, 7, 9]

# 13. Sum of numbers in range
def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum_of_numbers(5))    # 15
print(sum_of_numbers(10))   # 55
print(sum_of_numbers(100))  # 5050

# 14. Sum of odd numbers in range
def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(10))   # 25

# 15. Sum of even numbers in range
def sum_of_even(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(10))   # 30
