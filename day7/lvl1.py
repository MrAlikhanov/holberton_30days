# Day 7 - Sets - Level 1

# Initial set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Find the length of the set
print(len(it_companies))  # 7

# 2. Add 'Twitter' to the set
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once
it_companies.update(['Netflix', 'Tesla', 'Spotify'])
print(it_companies)

# 4. Remove one company from the set
it_companies.remove('IBM')
print(it_companies)

# 5. Difference between remove and discard
it_companies.remove('IBM')   # raises KeyError if item does not exist
it_companies.discard('IBM')  # does nothing if item does not exist
