
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

def XOR(a, b):
    p = AND(a, NOT(b))
    q = AND(NOT(a), b)
    return OR(p, q)


# Half Adder
def half_adder(a, b):
    sum_bit = XOR(a, b)
    carry = AND(a, b)
    return sum_bit, carry


# Full Adder
def full_adder(a, b, cin):
    sum1 = XOR(a, b)
    sum_bit = XOR(sum1, cin)

    carry1 = AND(a, b)
    carry2 = AND(sum1, cin)
    carry = OR(carry1, carry2)

    return sum_bit, carry


# Half Adder Truth Table
print("HALF ADDER")
print("A B | SUM CARRY")

for a in [0, 1]:
    for b in [0, 1]:
        s, c = half_adder(a, b)
        print(a, b, "|", s, c)


# Full Adder Truth Table
print("\nFULL ADDER")
print("A B Cin | SUM CARRY")

for a in [0, 1]:
    for b in [0, 1]:
        for cin in [0, 1]:
            s, c = full_adder(a, b, cin)
            print(a, b, cin, "|", s, c)
