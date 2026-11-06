
# Learning Rate Comparison in Perceptron

x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]

# Test different learning rates
for lr in [0.01, 0.1, 0.8]:

    # Initialize weights and bias
    w1 = 0
    w2 = 0
    b = 0

    # Training
    for epoch in range(100):

        error_count = 0

        for i in range(4):

            # Weighted sum
            net = x[i][0]*w1 + x[i][1]*w2 + b

            # Activation
            if net >= 0:
                pred = 1
            else:
                pred = 0

            # Error
            error = y[i] - pred

            # Update weights and bias
            w1 = w1 + lr * error * x[i][0]
            w2 = w2 + lr * error * x[i][1]
            b = b + lr * error

            if error != 0:
                error_count += 1

        # Check convergence
        if error_count == 0:
            break

    print("Learning Rate:", lr)
    print("Epochs:", epoch + 1)
    print("Final Weights:", w1, w2)
    print("Final Bias:", b)
    print("----------------------")
