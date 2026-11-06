# Decision Boundary using Perceptron

X = [[0,0], [0,1], [1,0], [1,1]]
Y = [0, 0, 0, 1]

w = [0, 0]
b = 0
lr = 0.1

# Training
for epoch in range(20):
    for i in range(4):
        net = w[0]*X[i][0] + w[1]*X[i][1] + b

        if net >= 0:
            pred = 1
        else:
            pred = 0

        error = Y[i] - pred

        w[0] += lr * error * X[i][0]
        w[1] += lr * error * X[i][1]
        b += lr * error

# Decision Boundary
print("Weights:", w)
print("Bias:", b)

print("Decision Boundary:")
print(w[0], "* x1 +", w[1], "* x2 +", b, "= 0")