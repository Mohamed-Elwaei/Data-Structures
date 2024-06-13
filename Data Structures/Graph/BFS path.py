from collections import deque

def bfs(graph, start, destination):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        if node == destination:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None



def bfs(graph, start, end):
    visited=set()
    queue=deque([start, [start]])  #Node and Path

    while queue:
        node, path=queue.popleft()

        if node==end:
            return path
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour, path+[neighbour])

    return None
# Sample input
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
destination_node = 'F'

shortest_path = bfs(graph, start_node, destination_node)
print(shortest_path)
