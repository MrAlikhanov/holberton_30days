
# From previous exercise
sisters = ('Aynur', 'Leyla')
brothers = ('Tural', 'Murad')
siblings = sisters + brothers
family_members = list(siblings)
family_members.append('Əli')
family_members.append('Günel')
family_members = tuple(family_members)

# 1. Unpack siblings and parents from family_members
*siblings_unpacked, father, mother = family_members
print("Siblings:", siblings_unpacked)  # ['Aynur', 'Leyla', 'Tural', 'Murad']
print("Father:", father)               # Əli
print("Mother:", mother)               # Günel

# 2. Create fruits, vegetables and animal products tuples, then join them
fruits = ('apple', 'banana', 'mango')
vegetables = ('carrot', 'potato', 'spinach')
animal_products = ('milk', 'cheese', 'egg')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Convert the tuple to a list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Slice out the middle item(s)
mid = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 == 0:
    middle = food_stuff_tp[mid - 1:mid + 1]
else:
    middle = food_stuff_tp[mid:mid + 1]
print("Middle:", middle)

# 5. Slice out the first three and last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three:", first_three)
print("Last three:", last_three)

# 6. Delete the tuple completely
del food_stuff_tp

# 7. Check if an item exists in the tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)  # False - Estonia is not a nordic country
print('Iceland' in nordic_countries)  # True - Iceland is a nordic country
