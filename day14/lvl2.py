# Day 14 - Higher Order Functions - Level 2

from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Full countries list (shortened here - use your countries.py file)
all_countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bangladesh', 'Belarus',
    'Belgium', 'Bosnia', 'Brazil', 'Bulgaria', 'Cambodia', 'Cameroon', 'Canada',
    'Chile', 'China', 'Colombia', 'Croatia', 'Cuba', 'Denmark', 'Ecuador',
    'Egypt', 'England', 'Estonia', 'Ethiopia', 'Finland', 'France', 'Georgia',
    'Germany', 'Ghana', 'Greece', 'Guatemala', 'Iceland', 'India', 'Indonesia',
    'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
    'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia',
    'Lebanon', 'Libya', 'Lithuania', 'Luxembourg', 'Malaysia', 'Mali', 'Malta',
    'Mexico', 'Moldova', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique',
    'Myanmar', 'Nepal', 'Netherlands', 'NewZealand', 'Nicaragua', 'Nigeria',
    'NorthMacedonia', 'Norway', 'Pakistan', 'Palestine', 'Panama', 'Paraguay',
    'Peru', 'Philippines', 'Poland', 'Portugal', 'Romania', 'Russia', 'Rwanda',
    'SaudiArabia', 'Scotland', 'Senegal', 'Serbia', 'Slovakia', 'Slovenia',
    'Somalia', 'SouthAfrica', 'Spain', 'Sudan', 'Sweden', 'Switzerland',
    'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Tunisia',
    'Turkey', 'Turkmenistan', 'Uganda', 'Ukraine', 'UAE', 'England', 'USA',
    'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]

# 1. Map - countries to uppercase
upper_countries = list(map(lambda c: c.upper(), countries))
print(upper_countries)

# 2. Map - numbers to squares
squared = list(map(lambda n: n**2, numbers))
print(squared)

# 3. Map - names to uppercase
upper_names = list(map(lambda n: n.upper(), names))
print(upper_names)

# 4. Filter - countries containing 'land'
land_countries = list(filter(lambda c: 'land' in c.lower(), countries))
print(land_countries)  # ['Finland', 'Iceland']

# 5. Filter - countries with exactly 6 characters
six_char = list(filter(lambda c: len(c) == 6, countries))
print(six_char)  # ['Sweden', 'Norway']

# 6. Filter - countries with 6 or more characters
six_or_more = list(filter(lambda c: len(c) >= 6, countries))
print(six_or_more)

# 7. Filter - countries starting with 'E'
e_countries = list(filter(lambda c: c.startswith('E'), countries))
print(e_countries)  # ['Estonia']

# 8. Chain map + filter + reduce
result = reduce(
    lambda a, b: a + b,
    filter(lambda x: x > 25, map(lambda x: x**2, numbers))
)
print(result)  # sum of squares greater than 25: 36+49+64+81+100 = 330

# 9. Get only string items from a list
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

mixed = [1, 'hello', True, 'world', 3.14, 'python']
print(get_string_lists(mixed))  # ['hello', 'world', 'python']

# 10. Reduce - sum all numbers
total = reduce(lambda a, b: a + b, numbers)
print(total)  # 55

# 11. Reduce - concatenate countries into a sentence
sentence = reduce(
    lambda a, b: a + ', ' + b,
    countries[:-1]
) + ', and ' + countries[-1] + ' are north European countries'
print(sentence)
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

# 12. Categorize countries by pattern
def categorize_countries(pattern):
    return list(filter(lambda c: pattern.lower() in c.lower(), all_countries))

print(categorize_countries('land'))   # ['Finland', 'Iceland', 'Ireland', ...]
print(categorize_countries('stan'))   # ['Afghanistan', 'Kazakhstan', ...]
print(categorize_countries('ia'))     # ['Albania', 'Armenia', 'Australia', ...]

# 13. Dictionary of starting letters and country counts
def count_by_first_letter(lst):
    result = {}
    for country in lst:
        letter = country[0].upper()
        result[letter] = result.get(letter, 0) + 1
    return result

letter_counts = count_by_first_letter(all_countries)
print(letter_counts)  # {'A': 8, 'B': 5, 'C': 8, ...}

# 14. First ten countries
def get_first_ten_countries():
    return all_countries[:10]

print(get_first_ten_countries())

# 15. Last ten countries
def get_last_ten_countries():
    return all_countries[-10:]

print(get_last_ten_countries())
