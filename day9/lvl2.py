
# Level 2

# 1. Grade calculator
score = int(input("Enter score: "))

if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
elif 60 <= score <= 69:
    grade = 'D'
else:
    grade = 'F'

print(f"Grade: {grade}")

# 2. Season checker
month = input("Enter month: ").strip().capitalize()

if month in ['September', 'October', 'November']:
    season = 'Autumn'
elif month in ['December', 'January', 'February']:
    season = 'Winter'
elif month in ['March', 'April', 'May']:
    season = 'Spring'
elif month in ['June', 'July', 'August']:
    season = 'Summer'
else:
    season = 'Unknown month'

print(f"Season: {season}")

# 3. Fruit list checker
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit name: ").strip().lower()

if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(f"Modified list: {fruits}")
