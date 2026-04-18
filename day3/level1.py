

import math

# 1. Age as integer
age = 25

# 2. Height as float
height = 5.9

# 3. Complex number
complex_num = 2 + 3j
print(type(complex_num))

# 4. Triangle area
base = float(input("Enter base: "))
height_tri = float(input("Enter height: "))
area = 0.5 * base * height_tri
print(f"The area of the triangle is {area}")

# 5. Triangle perimeter
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")

# 6. Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
rect_area = length * width
rect_perimeter = 2 * (length + width)
print(f"Area: {rect_area}, Perimeter: {rect_perimeter}")

# 7. Circle
pi = 3.14
radius = float(input("Enter radius: "))
circle_area = pi * radius * radius
circumference = 2 * pi * radius
print(f"Area: {circle_area}, Circumference: {circumference}")

# 8. y = 2x - 2 → slope, x-intercept, y-intercept
slope = 2
y_intercept = -2          # when x = 0
x_intercept = 1           # when y = 0 → 0 = 2x - 2 → x = 1
print(f"Slope: {slope}, X-intercept: {x_intercept}, Y-intercept: {y_intercept}")

# 9. Slope and Euclidean distance between (2,2) and (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope2 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Slope: {slope2}, Euclidean Distance: {distance}")

# 10. Compare slopes from 8 and 9
print(f"Slopes are equal: {slope == slope2}")

# 11. y = x^2 + 6x + 9  →  (x+3)^2 = 0  →  x = -3
x = -3
y = x**2 + 6*x + 9
print(f"y = {y} when x = {x}")   # y = 0

# 12. Falsy comparison: len('python') vs len('dragon')
print(len('python') != len('dragon'))   # False — both are 6

# 13. Check if 'on' is in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 14. Check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon"
print('jargon' in sentence)

# 15. There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')   # False

# 16. len('python') → float → string
length_python = len('python')
as_float = float(length_python)
as_string = str(as_float)
print(length_python, as_float, as_string)

# 17. Check if a number is even
num = 8
print(num % 2 == 0)

# 18. Floor division of 7 by 3 vs int(2.7)
print(7 // 3 == int(2.7))   # True (both are 2)

# 19. Check if type of '10' == type of 10
print(type('10') == type(10))   # False

# 20. Check if int('9.8') == 10  → raises ValueError, use float first
print(int(float('9.8')) == 10)   # False

# 21. Weekly earnings
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
earning = hours * rate
print(f"Your weekly earning is {earning}")

# 22. Seconds in a lifetime
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds.")

# 23. Table
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
