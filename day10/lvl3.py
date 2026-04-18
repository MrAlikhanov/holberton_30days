# Day 10 - Loops - Level 3

from countries import countries
from countries_data import data

# 1. Find all countries containing the word 'land'
land_countries = []
for country in countries:
    if 'land' in country.lower():
        land_countries.append(country)
print("Countries with 'land':", land_countries)

# 2. Reverse a fruit list using loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Reversed fruits:", reversed_fruits)

# 3a. Total number of languages in the data
all_languages = []
for country in data:
    for lang in country.get('languages', []):
        all_languages.append(lang)
print("Total number of languages (with duplicates):", len(all_languages))

# 3b. Ten most spoken languages
language_count = {}
for country in data:
    for lang in country.get('languages', []):
        if lang in language_count:
            language_count[lang] += 1
        else:
            language_count[lang] = 1

# sort by count descending
sorted_languages = []
for lang, count in language_count.items():
    sorted_languages.append((lang, count))

sorted_languages.sort(key=lambda x: x[1], reverse=True)

print("\nTop 10 most spoken languages:")
for lang, count in sorted_languages[:10]:
    print(f"  {lang}: {count} countries")

# 3c. Ten most populated countries
sorted_countries = []
for country in data:
    sorted_countries.append((country['name'], country.get('population', 0)))

sorted_countries.sort(key=lambda x: x[1], reverse=True)

print("\nTop 10 most populated countries:")
for name, pop in sorted_countries[:10]:
    print(f"  {name}: {pop:,}")
