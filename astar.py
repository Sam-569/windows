graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'E': 1},
    'D': {'G': 5},
    'E': {'G': 2},
    'G': {}
}

h = {
    'A': 6,
    'B': 5,
    'C': 3,
    'D': 4,
    'E': 2,
    'G': 0
}

start = 'A'
goal = 'G'

open_list = [start]
closed_list = []
g = {start: 0}
parent = {}

while open_list:
    current = min(open_list, key=lambda n: g[n] + h[n])
    open_list.remove(current)

    if current == goal:
        path = []
        while current in parent:
            path.append(current)
            current = parent[current]

        path.append(start)
        path.reverse()

        print("Path:", path)
        print("Cost:", g[goal])
        break

    closed_list.append(current)

    for neighbour, cost in graph[current].items():
        new_cost = g[current] + cost

        if neighbour not in g or new_cost < g[neighbour]:
            g[neighbour] = new_cost
            parent[neighbour] = current

            if neighbour not in closed_list and neighbour not in open_list:
                open_list.append(neighbour)