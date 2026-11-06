input_pattern = [1, -1, 1]
output_pattern = [-1, 1]

weights = [
    [0, 0],
    [0, 0],
    [0, 0]
]

# Store association using Hebbian learning
for i in range(3):
    for j in range(2):
        weights[i][j] += input_pattern[i] * output_pattern[j]

# Recall output
result = []

for j in range(2):
    total = 0

    for i in range(3):
        total += input_pattern[i] * weights[i][j]

    if total >= 0:
        result.append(1)
    else:
        result.append(-1)

print("Input:", input_pattern)
print("Recalled Output:", result)