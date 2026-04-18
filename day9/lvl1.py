# Day 9 - Conditionals - Level 1

# 1. Driving age checker
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more years to learn to drive.")

# -------------------------------------------------------

# 2. Age comparison
my_age = 25
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print(f"You are {diff} year older than me.")
    else:
        print(f"You are {diff} years older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    if diff == 1:
        print(f"You are {diff} year younger than me.")
    else:
        print(f"You are {diff} years younger than me.")
else:
    print("We are the same age!")

# 3. Compare two numbers
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")
