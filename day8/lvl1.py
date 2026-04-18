# Day 8 - Dictionaries

# 1. Empty dictionary
dog = {}

# 2. Add keys to dog dictionary
dog['name'] = 'Max'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3
print(dog)

# 3. Student dictionary
student = {
    'first_name': 'Anar',
    'last_name': 'Həsənov',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'Azerbaijan',
    'city': 'Baku',
    'address': 'Nizami Street 10'
}

# 4. Length of student dictionary
print(len(student))  # 9

# 5. Get skills value and check data type
skills = student['skills']
print(skills)           # ['Python', 'JavaScript']
print(type(skills))     # <class 'list'>

# 6. Modify skills by adding new skills
student['skills'].append('React')
student['skills'].append('Django')
print(student['skills'])  # ['Python', 'JavaScript', 'React', 'Django']

# 7. Get dictionary keys as a list
keys = list(student.keys())
print(keys)

# 8. Get dictionary values as a list
values = list(student.values())
print(values)

# 9. Change dictionary to a list of tuples using items()
items = list(student.items())
print(items)

# 10. Delete one item from the dictionary
del student['marital_status']
print(student)

# 11. Delete one of the dictionaries
del dog
