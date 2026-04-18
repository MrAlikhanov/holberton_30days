import json

# 1. Count lines and words in a text file
def count_lines_and_words(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
    print(f"File: {filename}")
    print(f"  Lines: {num_lines}")
    print(f"  Words: {num_words}\n")

count_lines_and_words('./data/obama_speech.txt')
count_lines_and_words('./data/michelle_obama_speech.txt')
count_lines_and_words('./data/donald_speech.txt')
count_lines_and_words('./data/melina_trump_speech.txt')


# 2. Ten most spoken languages from countries_data.json
def most_spoken_languages(filename, top=10):
    with open(filename, 'r') as f:
        data = json.load(f)

    language_count = {}
    for country in data:
        for lang in country.get('languages', []):
            language_count[lang] = language_count.get(lang, 0) + 1

    sorted_langs = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return [(count, lang) for lang, count in sorted_langs[:top]]

print(most_spoken_languages('./data/countries_data.json', 10))
print(most_spoken_languages('./data/countries_data.json', 3))


# 3. Ten most populated countries from countries_data.json
def most_populated_countries(filename, top=10):
    with open(filename, 'r') as f:
        data = json.load(f)

    sorted_countries = sorted(data, key=lambda x: x.get('population', 0), reverse=True)
    return [
        {'country': c['name'], 'population': c['population']}
        for c in sorted_countries[:top]
    ]

print(most_populated_countries('./data/countries_data.json', 10))
print(most_populated_countries('./data/countries_data.json', 3))
