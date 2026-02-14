# Simple A* Algorithm (Very Basic)

def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_list = [start]
    came = {}
    g = {start: 0}

    while open_list:
        # find node with lowest f = g + h
        current = open_list[0]
        for node in open_list:
            if g[node] + h(node, goal) < g[current] + h(current, goal):
                current = node

        open_list.remove(current)

        if current == goal:
            path = [current]
            while current in came:
                current = came[current]
                path.append(current)
            return path[::-1]

        x, y = current
        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                new_g = g[current] + 1
                if (nx, ny) not in g or new_g < g[(nx, ny)]:
                    g[(nx, ny)] = new_g
                    came[(nx, ny)] = current
                    if (nx, ny) not in open_list:
                        open_list.append((nx, ny))

    return None


grid = [
    [0,0,0],
    [1,0,1],
    [0,0,0]
]

print(astar(grid, (2,0), (0,2)))
