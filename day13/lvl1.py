# Day 13 - List Comprehension

# 1. Filter negative and zero
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [n for n in numbers if n <= 0]
print(negative_and_zero)  # [-4, -3, -2, -1, 0]

# 2. Flatten list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for sublist in list_of_lists for num in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. List of tuples with powers
powers = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
for t in powers:
    print(t)

# 4. Flatten countries to [NAME, CODE, CAPITAL]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_countries = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for item in countries
    for country, capital in item
]
print(flat_countries)
# [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# 5. Change list to list of dictionaries
dict_countries = [
    {'country': country.upper(), 'city': capital.upper()}
    for item in countries
    for country, capital in item
]
print(dict_countries)
# [{'country': 'FINLAND', 'city': 'HELSINKI'}, ...]

# 6. Concatenate names
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [
    f'{first} {last}'
    for item in names
    for first, last in item
]
print(full_names)
# ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# 7. Lambda for slope and y-intercept
# slope formula:     m = (y2 - y1) / (x2 - x1)
# y-intercept:       b = y - m * x

slope         = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept   = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1

print(slope(2, 2, 6, 10))           # 2.0
print(y_intercept(2, 2, 6, 10))     # -2.0
