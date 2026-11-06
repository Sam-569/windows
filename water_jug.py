def water_jug():
    A = 4
    B = 3
    target = 2

    queue = [(0, 0)]
    visited = []
    parent = {}

    while queue:
        a, b = queue.pop(0)

        if (a, b) in visited:
            continue

        visited.append((a, b))

        if a == target or b == target:
            path = []
            state = (a, b)

            while state in parent:
                path.append(state)
                state = parent[state]

            path.append((0, 0))
            path.reverse()

            for step in path:
                print(step)

            return

        x = min(a, B - b)
        y = min(b, A - a)

        next_states = [
            (A, b),
            (a, B),
            (0, b),
            (a, 0),
            (a - x, b + x),
            (a + y, b - y)
        ]

        for state in next_states:
            if state not in visited and state not in queue:
                parent[state] = (a, b)
                queue.append(state)


water_jug()