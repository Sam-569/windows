import math
import random

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def train(inputs, targets):
    w1 = [[0.2, 0.3], [0.4, 0.5]]
    w2 = [0.6, 0.7]

    b1 = [0.1, 0.1]
    b2 = 0.1
    rate = 0.5

    for epoch in range(10000):
        for i in range(len(inputs)):

            x1, x2 = inputs[i]

            # Forward propagation
            h1 = sigmoid(x1*w1[0][0] + x2*w1[0][1] + b1[0])
            h2 = sigmoid(x1*w1[1][0] + x2*w1[1][1] + b1[1])

            output = sigmoid(h1*w2[0] + h2*w2[1] + b2)

            # Calculate errors
            error = targets[i] - output

            # Backpropagation
            delta = error * output * (1-output)

            dh1 = delta * w2[0] * h1 * (1-h1)
            dh2 = delta * w2[1] * h2 * (1-h2)

            # Update output weights
            w2[0] += rate * delta * h1
            w2[1] += rate * delta * h2
            b2 += rate * delta

            # Update hidden weights
            w1[0][0] += rate * dh1 * x1
            w1[0][1] += rate * dh1 * x2
            w1[1][0] += rate * dh2 * x1
            w1[1][1] += rate * dh2 * x2

            b1[0] += rate * dh1
            b1[1] += rate * dh2

    return w1, w2, b1, b2


inputs = [[0,0], [0,1], [1,0], [1,1]]
targets = [0, 1, 1, 0]

w1, w2, b1, b2 = train(inputs, targets)

print("XOR Predictions:")

for x1, x2 in inputs:
    h1 = sigmoid(x1*w1[0][0] + x2*w1[0][1] + b1[0])
    h2 = sigmoid(x1*w1[1][0] + x2*w1[1][1] + b1[1])

    output = sigmoid(h1*w2[0] + h2*w2[1] + b2)

    print(x1, x2, ":", round(output, 3))