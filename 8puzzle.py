start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

queue = [start]
visited = []
parent = {}

while queue:
    state = queue.pop(0)

    if state in visited:
        continue

    visited.append(state)

    if state == goal:
        path = []
        while state in parent:
            path.append(state)
            state = parent[state]

        path.append(start)
        path.reverse()

        for step in path:
            print(step[0:3])
            print(step[3:6])
            print(step[6:9])
            print()

        break

    pos = state.index(0)
    row = pos // 3
    col = pos % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            temp = list(state)

            temp[pos], temp[new_pos] = temp[new_pos], temp[pos]
            new_state = tuple(temp)

            if new_state not in visited and new_state not in queue:
                queue.append(new_state)
                parent[new_state] = state