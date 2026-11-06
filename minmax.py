# Max-Min Composition

R = [[0.2, 0.7],
     [0.5, 0.4]]

S = [[0.6, 0.3],
     [0.8, 0.9]]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = max(
            min(R[i][0], S[0][j]),
            min(R[i][1], S[1][j])
        )

print("Max-Min Composition:")
for row in result:
    print(row)