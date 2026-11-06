
# McCulloch-Pitts Neuron

def mp_neuron(inputs, weights, threshold):

    total = 0

    for i in range(len(inputs)):
        total = total + inputs[i] * weights[i]

    if total >= threshold:
        return 1
    else:
        return 0


# AND Gate
def AND(a, b):
    return mp_neuron([a, b], [1, 1], 2)


# OR Gate
def OR(a, b):
    return mp_neuron([a, b], [1, 1], 1)


# NOT Gate
def NOT(a):
    return mp_neuron([a], [-1], 0)


# NAND Gate
def NAND(a, b):
    return mp_neuron([a, b], [-1, -1], -1)


# Display outputs
print("AND GATE")
for a in [0, 1]:
    for b in [0, 1]:
        print(a, b, "=", AND(a, b))

print("\nOR GATE")
for a in [0, 1]:
    for b in [0, 1]:
        print(a, b, "=", OR(a, b))

print("\nNOT GATE")
for a in [0, 1]:
    print(a, "=", NOT(a))

print("\nNAND GATE")
for a in [0,1]:
    for b in [0,1]:
        print(a,b,"=",NAND(a,b))