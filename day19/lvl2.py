import re
import json
from collections import Counter

# 1. Extract email addresses from email_exchange_big.txt
def extract_emails(filename):
    with open(filename, 'r') as f:
        content = f.read()
    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', content)
    return list(set(emails))  # unique emails

emails = extract_emails('./data/email_exchange_big.txt')
print(f"Found {len(emails)} unique emails")
print(emails[:5])


# 2. Find most common words in a file or string
def find_most_common_words(source, top=10):
    # check if source is a file or string
    try:
        with open(source, 'r') as f:
            content = f.read()
    except (FileNotFoundError, OSError):
        content = source

    # clean and split
    words = re.sub(r'[^a-zA-Z ]', '', content).lower().split()
    count = Counter(words)
    sorted_words = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [(count, word) for word, count in sorted_words[:top]]

print(find_most_common_words('./data/sample.txt', 10))
print(find_most_common_words('./data/sample.txt', 5))


# 3. Most frequent words in speeches
print("\n--- Obama's Speech ---")
print(find_most_common_words('./data/obama_speech.txt', 10))

print("\n--- Michelle's Speech ---")
print(find_most_common_words('./data/michelle_obama_speech.txt', 10))

print("\n--- Trump's Speech ---")
print(find_most_common_words('./data/donald_speech.txt', 10))

print("\n--- Melina's Speech ---")
print(find_most_common_words('./data/melina_trump_speech.txt', 10))


# 4. Text similarity checker
def clean_text(text):
    return re.sub(r'[^a-zA-Z ]', '', text).lower().split()

def remove_stop_words(words, stop_words):
    return [w for w in words if w not in stop_words]

def check_text_similarity(file1, file2):
    # load stop words
    with open('./data/stop_words.py', 'r') as f:
        content = f.read()
    stop_words = re.findall(r"'(\w+)'", content)

    with open(file1, 'r') as f:
        words1 = remove_stop_words(clean_text(f.read()), stop_words)
    with open(file2, 'r') as f:
        words2 = remove_stop_words(clean_text(f.read()), stop_words)

    set1 = set(words1)
    set2 = set(words2)

    common = set1.intersection(set2)
    similarity = len(common) / len(set1.union(set2)) * 100

    print(f"Common words: {len(common)}")
    print(f"Similarity: {similarity:.2f}%")
    return similarity

check_text_similarity('./data/michelle_obama_speech.txt', './data/melina_trump_speech.txt')


# 5. Ten most repeated words in Romeo and Juliet
print("\n--- Romeo and Juliet ---")
print(find_most_common_words('./data/romeo_and_juliet.txt', 10))


# 6. Hacker News CSV analysis
def analyze_hacker_news(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    python_count = sum(1 for line in lines if re.search(r'python', line, re.IGNORECASE))
    javascript_count = sum(1 for line in lines if re.search(r'javascript', line, re.IGNORECASE))
    java_only_count = sum(
        1 for line in lines
        if re.search(r'\bjava\b', line, re.IGNORECASE)
        and not re.search(r'javascript', line, re.IGNORECASE)
    )

    print(f"\n--- Hacker News Analysis ---")
    print(f"Lines with Python:              {python_count}")
    print(f"Lines with JavaScript:          {javascript_count}")
    print(f"Lines with Java (not JS):       {java_only_count}")

analyze_hacker_news('./data/hacker_news.csv')
