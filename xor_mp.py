# McCulloch-Pitts Neuron

def mp_neuron(inputs, weights, threshold):
    total = 0

    for i in range(len(inputs)):
        total += inputs[i] * weights[i]

    if total >= threshold:
        return 1
    else:
        return 0


# Basic Logic Gates
def AND(a, b):
    return mp_neuron([a, b], [1, 1], 2)

def OR(a, b):
    return mp_neuron([a, b], [1, 1], 1)

def NOT(a):
    return mp_neuron([a], [-1], 0)


# XOR Gate
def XOR(a, b):
    p = AND(a, NOT(b))
    q = AND(NOT(a), b)
    return OR(p, q)


# XOR Truth Table
print("XOR GATE")
print("A B | XOR")

for a in [0, 1]:
    for b in [0, 1]:
        print(a, b, "|", XOR(a, b))