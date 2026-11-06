countries = [
  [1,-1,-1],
  [-1,1,-1],
  [-1,-1,1]
]

cities = [
  [1,-1,-1],
  [-1,1,-1],
  [-1,-1,1]
]


names = ["India", "Japan", "France"]
capital_names = ["Delhi", "Tokyo", "Paris"]

weights = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for p in range (3):
  for i in range (3):
    for j in range (3):
      weights[i][j] += countries[p][i] * cities[p][j]


for p in range(3):
  output = []

  for j in range(3):
    total=0
    for i in range(3):
      total += countries[p][i] * weights[i][j]
    output.append(1 if total >= 0 else -1)

    print(names[p], "=", capital_names[output.index(1)])
    