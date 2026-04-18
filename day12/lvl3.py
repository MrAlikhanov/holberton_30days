import random

# 1. Shuffle a list
def shuffle_list(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled

print(shuffle_list([1, 2, 3, 4, 5]))        # e.g. [3, 1, 5, 2, 4]
print(shuffle_list(['a', 'b', 'c', 'd']))   # e.g. ['c', 'a', 'd', 'b']

# 2. Seven unique random numbers from 0-9
def seven_unique_numbers():
    return random.sample(range(10), 7)

print(seven_unique_numbers())  # e.g. [3, 7, 0, 9, 1, 5, 2]
