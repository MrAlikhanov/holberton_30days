# 1. Sum of all numbers from 0 to 100
total = 0
for i in range(101):
    total += i
print(f"The sum of all numbers is {total}.")

# 2. Sum of evens and odds from 0 to 100
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i
print(f"The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.")
