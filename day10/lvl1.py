# Day 10 - Loops - Level 1

# 1. Iterate 0 to 10
# for loop
for i in range(11):
    print(i, end=' ')
print()

# while loop
i = 0
while i <= 10:
    print(i, end=' ')
    i += 1
print()

# -------------------------------------------------------

# 2. Iterate 10 to 0
# for loop
for i in range(10, -1, -1):
    print(i, end=' ')
print()

# while loop
i = 10
while i >= 0:
    print(i, end=' ')
    i -= 1
print()

# -------------------------------------------------------

# 3. Triangle
for i in range(1, 8):
    print('#' * i)

# -------------------------------------------------------

# 4. 8x8 hash grid
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

# -------------------------------------------------------

# 5. Multiplication pattern
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# -------------------------------------------------------

# 6. Iterate through list
frameworks = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for framework in frameworks:
    print(framework)

# -------------------------------------------------------

# 7. Even numbers from 0 to 100
for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=' ')
print()

# -------------------------------------------------------

# 8. Odd numbers from 0 to 100
for i in range(0, 101):
    if i % 2 != 0:
        print(i, end=' ')
print()
