import heapq

def a_star(graph, start, goal, heuristic):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path
        visited.add(node)

        for neighbor, weight in graph[node]:
            heapq.heappush(pq, (cost + weight + heuristic[neighbor], neighbor, path))

    return None

def main():
    graph = {
        'A': [('B',1), ('C',3)],
        'B': [('D',1)],
        'C': [('D',1)],
        'D': []
    }
    heuristic = {'A':3,'B':2,'C':1,'D':0}
    print(a_star(graph, 'A', 'D', heuristic))

main()
