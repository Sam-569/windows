# Max-Product Composition

R = [[0.2, 0.7],
     [0.5, 0.4]]

S = [[0.6, 0.3],
     [0.8, 0.9]]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = max(
            R[i][0] * S[0][j],
            R[i][1] * S[1][j]
        )

print("Max-Product Composition:")
for row in result:
    print(row)