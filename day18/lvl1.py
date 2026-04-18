paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Clean punctuation and split into words
words = paragraph.replace('.', '').replace(',', '').split()

# Count each word
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Sort by count descending
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Format as (count, word)
result = [(count, word) for word, count in sorted_words]

print(result)
print(f"\nMost frequent word: '{result[0][1]}' with {result[0][0]} occurrences")
