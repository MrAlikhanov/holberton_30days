
first_name = "John"
last_name = "Doe"
full_name = "John Doe"
country = "Azerbaijan"
city = "Baku"
age = 25
year = 2026
is_married = False
is_true = True
is_light_on = True

# 1. Check data types using type()
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# 2. Find the length of first name
print(len(first_name))

# 3. Compare the length of first name and last name
print(len(first_name) == len(last_name))   # Are they equal?
print(len(first_name) > len(last_name))    # Is first name longer?
print(len(first_name) < len(last_name))    # Is last name longer?

# 4. Declare num_one and num_two
num_one = 5
num_two = 4

# 5. Addition
total = num_one + num_two
print("Total:", total)

# 6. Subtraction
diff = num_one - num_two
print("Difference:", diff)

# 7. Multiplication
product = num_one * num_two
print("Product:", product)

# 8. Division
division = num_one / num_two
print("Division:", division)

# 9. Modulus
remainder = num_two % num_one
print("Remainder:", remainder)

# 10. Exponent
exp = num_one ** num_two
print("Exponent:", exp)

# 11. Floor division
floor_division = num_one // num_two
print("Floor Division:", floor_division)

# 12. Circle calculations
PI = 3.14159

# 12.1 Area of circle (radius = 30)
radius = 30
area_of_circle = PI * radius ** 2
print("Area of Circle:", area_of_circle)

# 12.2 Circumference of circle
circum_of_circle = 2 * PI * radius
print("Circumference of Circle:", circum_of_circle)

# 12.3 Take radius as user input and calculate area
radius = float(input("Enter the radius: "))
area_of_circle = PI * radius ** 2
print("Area of Circle:", area_of_circle)

# 13. Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

# 14. Python reserved keywords
help('keywords')
