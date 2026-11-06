# Student Pass/Fail Classification

X = [[1, 40], [2, 50], [3, 60], [4, 70],
     [5, 80], [6, 90]]

Y = [0, 0, 0, 1, 1, 1]

w = [0, 0]
b = 0
lr = 0.01

# Training
for epoch in range(100):
    for i in range(len(X)):
        net = w[0]*X[i][0] + w[1]*X[i][1] + b

        if net >= 0:
            pred = 1
        else:
            pred = 0

        error = Y[i] - pred

        w[0] += lr * error * X[i][0]
        w[1] += lr * error * X[i][1]
        b += lr * error

# Testing
hours = 4
attendance = 75

net = w[0]*hours + w[1]*attendance + b

if net >= 0:
    print("Pass")
else:
    print("Fail") 