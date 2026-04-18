# Day 7 - Sets - Level 2

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 1. Join A and B (union)
print(A.union(B))          # {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)               # same result with | operator

# 2. Find A intersection B (common elements)
print(A.intersection(B))   # {4, 5}
print(A & B)               # same result with & operator

# 3. Is A subset of B
print(A.issubset(B))       # False - A has elements not in B

# 4. Are A and B disjoint sets (no common elements)
print(A.isdisjoint(B))     # False - they share 4 and 5

# 5. Join A with B and B with A
A.update(B)                # A now contains all elements from both
print(A)                   # {1, 2, 3, 4, 5, 6, 7, 8}

B.update(A)                # B now contains all elements from both
print(B)                   # {1, 2, 3, 4, 5, 6, 7, 8}

# 6. Symmetric difference (elements in A or B but not in both)
A = {1, 2, 3, 4, 5}       # reset A
B = {4, 5, 6, 7, 8}       # reset B
print(A.symmetric_difference(B))  # {1, 2, 3, 6, 7, 8}
print(A ^ B)               # same result with ^ operator

# 7. Delete the sets completely
del A
del B
