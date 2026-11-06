data = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]
]

labels = [1, 1, 0, 0]

weights = [
    [0.8, 0.8],
    [0.2, 0.2]
]

classes = [1, 0]
lr = 0.1

for epoch in range(10):
    for i in range(len(data)):
        x = data[i]

        winner = 0
        min_dist = 999

        for j in range(len(weights)):
            dist = (x[0] - weights[j][0])**2 + (x[1] - weights[j][1])**2

            if dist < min_dist:
                min_dist = dist
                winner = j

        for k in range(2):
            if classes[winner] == labels[i]:
                weights[winner][k] += lr * (x[k] - weights[winner][k])
            else:
                weights[winner][k] -= lr * (x[k] - weights[winner][k])

print("Final Weights:")
for w in weights:
    print(w)

print("Predictions:")
for x in data:
    winner = 0
    min_dist = 999

    for j in range(len(weights)):
        dist = (x[0] - weights[j][0])**2 + (x[1] - weights[j][1])**2

        if dist < min_dist:
            min_dist = dist
            winner = j

    print(x, "=", classes[winner])