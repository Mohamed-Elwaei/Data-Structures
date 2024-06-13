from collections import deque

def BFS_shortest_path(graph, source):
    distances = {}
    queue = deque()   # A queue data structure to store the vertices
    visited = set()   # A set to keep track of visited vertices

    for vertex in graph.keys():
        distances[vertex] = float('inf')

    distances[source] = 0
    visited.add(source)
    queue.append(source)

    while queue:
        current_vertex = queue.popleft()

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                distances[neighbor] = distances[current_vertex] + 1
                visited.add(neighbor)
                queue.append(neighbor)

    return distances




# Example graph represented as an adjacency list
graph = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0, 3],
    3: [0, 1, 2, 4],
    4: [3]
}

source_vertex = 0
shortest_distances = BFS_shortest_path(graph, source_vertex)

# Print the shortest distances from the source vertex to all other vertices
print("Shortest Distances from vertex", source_vertex)
for vertex, distance in shortest_distances.items():
    print(f"To vertex {vertex}: Distance {distance}")
