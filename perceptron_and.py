
# Single Layer Perceptron - AND Gate

# Input dataset
x = [[0, 0],
     [0, 1],
     [1, 0],
     [1, 1]]

# Expected output
y = [0, 0, 0, 1]

# Initialize weights and bias
w1 = 0
w2 = 0
b = 0

# Learning rate
lr = 0.1

# Training
for epoch in range(100):

    error_count = 0

    for i in range(4):

        # Calculate weighted sum
        net = x[i][0]*w1 + x[i][1]*w2 + b

        # Activation function
        if net >= 0:
            pred = 1
        else:
            pred = 0

        # Calculate error
        error = y[i] - pred

        # Update weights and bias
        w1 = w1 + lr * error * x[i][0]
        w2 = w2 + lr * error * x[i][1]
        b = b + lr * error

        if error != 0:
            error_count += 1

    print("Epoch:", epoch+1)
    print("Weights:", w1, w2)
    print("Bias:", b)
    print("Errors:", error_count)
    print("----------------")

    # Stop if no errors
    if error_count == 0:
        break


# Test final output
print("\nFINAL OUTPUT")

for i in range(4):

    net = x[i][0]*w1 + x[i][1]*w2 + b

    if net >= 0:
        pred = 1
    else:
        pred = 0

    print(x[i], "=", pred)
