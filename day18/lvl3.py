import re
from collections import Counter

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    # Remove all special characters except letters and spaces
    cleaned = re.sub(r'[^a-zA-Z ]', '', text)
    # Remove extra spaces
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def most_frequent_words(text, top=3):
    words = text.split()
    count = Counter(words)
    sorted_words = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [(count, word) for word, count in sorted_words[:top]]

cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))
