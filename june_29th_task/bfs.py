from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

def bfs(graph, start):

    queue = deque([start])

    visited = {start}

    while queue:

        node = queue.popleft()

        print(node)

        for neighbour in graph[node]:

            if neighbour not in visited:

                visited.add(neighbour)

                queue.append(neighbour)

bfs(graph, "A")