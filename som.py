data = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]
]

weights = [
    [0.2, 0.3],
    [0.6, 0.5],
    [0.8, 0.9]
]

lr = 0.5

for epoch in range(10):
    for x in data:

        winner = 0
        min_dist = 999

        for i in range(len(weights)):
            dist = (x[0] - weights[i][0])**2 + (x[1] - weights[i][1])**2

            if dist < min_dist:
                min_dist = dist
                winner = i

        for j in range(2):
            weights[winner][j] += lr * (x[j] - weights[winner][j])

print("Final Weights:")
for w in weights:
    print(w)