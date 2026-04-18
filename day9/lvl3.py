
# Level 3

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check if skills key exists and print middle skill
if 'skills' in person:
    skills = person['skills']
    mid = len(skills) // 2
    print(f"Middle skill: {skills[mid]}")  # MongoDB

# 2. Check if person has Python skill
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill")
    else:
        print("The person does not have Python skill")

# 3. Determine developer title based on skills
if 'skills' in person:
    skills = set(person['skills'])

    if skills == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print('He is a fullstack developer')
    else:
        print('unknown title')

# 4. Print info if married and lives in Finland
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
