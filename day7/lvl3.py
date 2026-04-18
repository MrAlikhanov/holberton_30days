
# 1. Convert ages list to set and compare lengths
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages_set = set(ages)

print("List length:", len(ages))      # 10
print("Set length:", len(ages_set))   # 6 - duplicates removed
print("List is bigger:", len(ages) > len(ages_set))  # True
