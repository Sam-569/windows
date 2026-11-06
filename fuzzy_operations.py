# Fuzzy Set Operations

A = {"Low": 0.2, "Medium": 0.6, "High": 0.9}
B = {"Low": 0.5, "Medium": 0.4, "High": 0.7}

union = {}
intersection = {}
complement = {}

for x in A:
    union[x] = max(A[x], B[x])
    intersection[x] = min(A[x], B[x])
    complement[x] = 1 - A[x]

print("Union:", union)
print("Intersection:", intersection)
print("Complement:", complement)