countries = [
    [1, -1, -1],
    [-1, 1, -1],
    [-1, -1, 1]
]

capitals = [
    [1, -1, -1],
    [-1, 1, -1],
    [-1, -1, 1]
]

names = ["India", "Japan", "France"]
capital_names = ["Delhi", "Tokyo", "Paris"]

# Initialize weights
weights = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Hebbian learning
for p in range(3):
    for i in range(3):
        for j in range(3):
            weights[i][j] += countries[p][i] * capitals[p][j]

# Recall capital from country
for p in range(3):
    output = []

    for j in range(3):
        total = 0
        for i in range(3):
            total += countries[p][i] * weights[i][j]

        output.append(1 if total >= 0 else -1)

    print(names[p], "=", capital_names[output.index(1)])

# Recall country from capital
print("\nReverse Association:")

for p in range(3):
    output = []

    for i in range(3):
        total = 0
        for j in range(3):
            total += capitals[p][j] * weights[i][j]

        output.append(1 if total >= 0 else -1)

    print(capital_names[p], "=", names[output.index(1)])