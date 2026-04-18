

# 1. Concatenate 'Thirty', 'Days', 'Of', 'Python'
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# 2. Concatenate 'Coding', 'For', 'All'
print('Coding' + ' ' + 'For' + ' ' + 'All')

# 3. Declare company variable
company = "Coding For All"

# 4. Print company
print(company)

# 5. Print length
print(len(company))

# 6. Uppercase
print(company.upper())

# 7. Lowercase
print(company.lower())

# 8. capitalize, title, swapcase
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Slice out first word
print(company[:6])   # 'Coding'

# 10. Check if 'Coding' is in the string
print(company.find('Coding'))    # 0
print(company.index('Coding'))   # 0

# 11. Replace 'Coding' with 'Python'
print(company.replace('Coding', 'Python'))

# 12. Change "Python for Everyone" to "Python for All"
print("Python for Everyone".replace('Everyone', 'All'))

# 13. Split by space
print(company.split())

# 14. Split at comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

# 15. Character at index 0
print(company[0])   # 'C'

# 16. Last index
print(len(company) - 1)   # 13

# 17. Character at index 10
print(company[10])   # 'A'

# 18. Acronym for 'Python For Everyone'
pfe = 'Python For Everyone'
print(''.join([word[0].upper() for word in pfe.split()]))   # PFE

# 19. Acronym for 'Coding For All'
cfa = 'Coding For All'
print(''.join([word[0].upper() for word in cfa.split()]))   # CFA

# 20. Position of first 'C' in 'Coding For All'
print(company.index('C'))   # 0

# 21. Position of first 'F' in 'Coding For All'
print(company.index('F'))   # 7

# 22. Last occurrence of 'l' in 'Coding For All People'
print('Coding For All People'.rfind('l'))   # 13

# 23. First occurrence of 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))   # 31

# 24. Last occurrence of 'because'
print(sentence.rindex('because'))   # 47

# 25 & 27. Slice out 'because because because'
start = sentence.find('because')
print(sentence[start:start + 23])   # 'because because because'

# 26. Position of first 'because'
print(sentence.index('because'))   # 31

# 28. Does 'Coding For All' start with 'Coding'?
print(company.startswith('Coding'))   # True

# 29. Does 'Coding For All' end with 'coding'?
print(company.endswith('coding'))   # False (case-sensitive!)

# 30. Remove trailing spaces
spaced = '   Coding For All      '
print(spaced.strip())

# 31. isidentifier check
print('30DaysOfPython'.isidentifier())      # False (rəqəmlə başlayır)
print('thirty_days_of_python'.isidentifier())  # True

# 32. Join list with ' # '
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# 33. New line escape sequence
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34. Tab escape sequence
print('Name\t\tAge\tCountry\t\tCity')
print('Asabeneh\t250\tFinland\t\tHelsinki')

# 35. String formatting - circle area
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

# 36. String formatting - arithmetic
a, b = 8, 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
