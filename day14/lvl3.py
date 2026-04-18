# Day 14 - Higher Order Functions - Level 3

from functools import reduce

# Import your countries data file or paste data here
# from countries_data import data

data = [
    {'name': 'Afghanistan', 'capital': 'Kabul',         'languages': ['Pashto', 'Uzbek', 'Turkmen'],    'population': 27657145},
    {'name': 'Albania',     'capital': 'Tirana',         'languages': ['Albanian', 'Greek'],              'population': 2886026},
    {'name': 'Algeria',     'capital': 'Algiers',        'languages': ['Arabic'],                         'population': 40400000},
    {'name': 'Andorra',     'capital': 'Andorra la Vella','languages': ['Catalan'],                       'population': 78014},
    {'name': 'Angola',      'capital': 'Luanda',         'languages': ['Portuguese'],                     'population': 25868000},
    {'name': 'Argentina',   'capital': 'Buenos Aires',   'languages': ['Spanish'],                        'population': 43590400},
    {'name': 'Armenia',     'capital': 'Yerevan',        'languages': ['Armenian'],                       'population': 2994400},
    {'name': 'Australia',   'capital': 'Canberra',       'languages': ['English'],                        'population': 24117360},
    {'name': 'Austria',     'capital': 'Vienna',         'languages': ['German'],                         'population': 8794267},
    {'name': 'Azerbaijan',  'capital': 'Baku',           'languages': ['Azerbaijani'],                    'population': 9939800},
    {'name': 'Brazil',      'capital': 'Brasilia',       'languages': ['Portuguese'],                     'population': 209288278},
    {'name': 'China',       'capital': 'Beijing',        'languages': ['Chinese'],                        'population': 1409517397},
    {'name': 'Denmark',     'capital': 'Copenhagen',     'languages': ['Danish'],                         'population': 5717014},
    {'name': 'Egypt',       'capital': 'Cairo',          'languages': ['Arabic'],                         'population': 92442547},
    {'name': 'Estonia',     'capital': 'Tallinn',        'languages': ['Estonian'],                       'population': 1315944},
    {'name': 'Finland',     'capital': 'Helsinki',       'languages': ['Finnish', 'Swedish'],             'population': 5491817},
    {'name': 'France',      'capital': 'Paris',          'languages': ['French'],                         'population': 66710000},
    {'name': 'Germany',     'capital': 'Berlin',         'languages': ['German'],                         'population': 81770900},
    {'name': 'India',       'capital': 'New Delhi',      'languages': ['Hindi', 'English'],               'population': 1295210000},
    {'name': 'Indonesia',   'capital': 'Jakarta',        'languages': ['Indonesian'],                     'population': 258705000},
    {'name': 'Iran',        'capital': 'Tehran',         'languages': ['Persian'],                        'population': 79369900},
    {'name': 'Japan',       'capital': 'Tokyo',          'languages': ['Japanese'],                       'population': 126960000},
    {'name': 'Nigeria',     'capital': 'Abuja',          'languages': ['English'],                        'population': 186988000},
    {'name': 'Norway',      'capital': 'Oslo',           'languages': ['Norwegian'],                      'population': 5223256},
    {'name': 'Pakistan',    'capital': 'Islamabad',      'languages': ['Urdu', 'English'],                'population': 194125062},
    {'name': 'Russia',      'capital': 'Moscow',         'languages': ['Russian'],                        'population': 146599183},
    {'name': 'Spain',       'capital': 'Madrid',         'languages': ['Spanish'],                        'population': 46438422},
    {'name': 'Sweden',      'capital': 'Stockholm',      'languages': ['Swedish'],                        'population': 9894888},
    {'name': 'Turkey',      'capital': 'Ankara',         'languages': ['Turkish'],                        'population': 79814871},
    {'name': 'USA',         'capital': 'Washington DC',  'languages': ['English'],                        'population': 323947000},
]

# 1a. Sort by name
sorted_by_name = sorted(data, key=lambda c: c['name'])
print("--- Sorted by Name ---")
for c in sorted_by_name:
    print(c['name'])

# 1b. Sort by capital
sorted_by_capital = sorted(data, key=lambda c: c['capital'])
print("\n--- Sorted by Capital ---")
for c in sorted_by_capital:
    print(f"{c['name']} - {c['capital']}")

# 1c. Sort by population
sorted_by_population = sorted(data, key=lambda c: c['population'], reverse=True)
print("\n--- Sorted by Population ---")
for c in sorted_by_population:
    print(f"{c['name']}: {c['population']:,}")

# 2. Ten most spoken languages
def most_spoken_languages(top=10):
    language_count = {}
    for country in data:
        for lang in country.get('languages', []):
            language_count[lang] = language_count.get(lang, 0) + 1

    sorted_langs = sorted(language_count.items(), key=lambda x: x[1], reverse=True)

    print(f"\n--- Top {top} Most Spoken Languages ---")
    for lang, count in sorted_langs[:top]:
        print(f"{lang}: {count} countries")

most_spoken_languages(10)

# 3. Ten most populated countries
def most_populated_countries(top=10):
    sorted_countries = sorted(data, key=lambda c: c['population'], reverse=True)

    print(f"\n--- Top {top} Most Populated Countries ---")
    for country in sorted_countries[:top]:
        print(f"{country['name']}: {country['population']:,}")

most_populated_countries(10)
