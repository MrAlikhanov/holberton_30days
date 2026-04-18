import requests
import re
import statistics
from collections import Counter
from bs4 import BeautifulSoup

# --- 1. Romeo and Juliet: 10 Most Frequent Words ---
def romeo_juliet_frequent_words():
    print("--- 1. Romeo and Juliet: En çox işlənən 10 söz ---")
    url = 'http://www.gutenberg.org/files/1112/1112.txt'
    try:
        response = requests.get(url)
        text = response.text
        words = re.findall(r'\b\w+\b', text.lower())
        most_common = Counter(words).most_common(10)
        for word, count in most_common:
            print(f"{word}: {count}")
    except Exception as e:
        print(f"Xəta baş verdi: {e}")
    print("\n")

# --- 2. Cats API: Statistics & Frequency Table ---
def cats_api_analysis():
    print("--- 2. Cats API Analizi ---")
    url = 'https://api.thecatapi.com/v1/breeds'
    response = requests.get(url)
    cats = response.json()

    weights = []
    lifespans = []
    
    print("Country vs Breed Frequency Table:")
    for cat in cats:
        # Frequency table (Ölkə və Cins)
        print(f"Country: {cat['origin']} | Breed: {cat['name']}")
        
        # Weight (metric) parse
        w_range = cat['weight']['metric'].split(' - ')
        weights.append((float(w_range[0]) + float(w_range[-1])) / 2)
        
        # Lifespan parse
        l_range = cat['lifespan'].replace(' ', '').split('-')
        lifespans.append((float(l_range[0]) + float(l_range[-1])) / 2)

    def print_stats(data, title):
        print(f"\n{title} Statistikası:")
        print(f"Min: {min(data)}")
        print(f"Max: {max(data)}")
        print(f"Mean (Orta): {statistics.mean(data):.2f}")
        print(f"Median: {statistics.median(data)}")
        print(f"Standard Deviation: {statistics.stdev(data):.2f}")

    print_stats(weights, "Çəki (Metric)")
    print_stats(lifespans, "Ömür Müddəti (İl)")
    print("\n")

# --- 3. Countries API Analysis ---
def countries_api_analysis():
    print("--- 3. Countries API Analizi ---")
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)
    countries = response.json()

    # 10 Largest Countries
    largest = sorted(countries, key=lambda x: x.get('area', 0) if x.get('area') else 0, reverse=True)[:10]
    print("En böyük 10 ölkə:", [c['name']['common'] for c in largest])

    # Languages
    all_langs = []
    for c in countries:
        if 'languages' in c:
            all_langs.extend(c['languages'].values())

    print(f"Ümumi dillərin sayı: {len(set(all_langs))}")
    print("En çox danışılan 10 dil:", Counter(all_langs).most_common(10))
    print("\n")

# --- 4. UCI Datasets Scraping ---
def uci_datasets_scraping():
    print("--- 4. UCI Dataset Scraping ---")
    url = 'https://archive.ics.uci.edu/datasets'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # UCI-nın yeni dizaynına uyğun olaraq linkləri və ya başlıqları çəkirik
        datasets = soup.find_all('a', class_='link') # Bu hissə sayt dəyişdikcə yenilənməlidir
        
        print("UCI-dan bəzi dataset adları:")
        for ds in datasets[:10]:
            print("- " + ds.text.strip())
    except Exception as e:
        print("UCI saytına qoşularkən xəta (və ya BS4 selector dəyişib).")
    print("\n")

# Hamısını icra et
if __name__ == "__main__":
    romeo_juliet_frequent_words()
    cats_api_analysis()
    countries_api_analysis()
    uci_datasets_scraping()
