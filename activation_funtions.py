import math

def binary_step(x):
    if x >= 0:
        return 1
    else:
        return 0

def bipolar_step(x):
    if x >= 0:
        return 1
    else:
        return -1

def symmetric_hard_limit(x):
    if x >= 2:
        return 1
    else:
        return -1

def saturating_linear(x):
    if x < -1:
        return -1
    elif x > 1:
        return 1
    else:
        return x

def tansig(x):
    return math.tanh(x)

def log_sigmoid(x):
    return 1 / (1 + math.exp(-x))


values = [-2, -1, 0, 1, 2]

for x in values:
    print("Input:", x)
    print("Binary Step:", binary_step(x))
    print("Bipolar Step:", bipolar_step(x))
    print("Symmetric Hard Limit:", symmetric_hard_limit(x))
    print("Saturating Linear:", saturating_linear(x))
    print("Tansig:", round(tansig(x), 3))
    print("Log Sigmoid:", round(log_sigmoid(x), 3))
    print("--------------------------")