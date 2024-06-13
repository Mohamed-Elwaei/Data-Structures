import heapq


def dijkstra(graph, start):
    # Initialize distances with infinity for all nodes except the start node,
    # which is initialized with a distance of 0.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to store nodes and their tentative distances.
    priority_queue = [(0, start)]
 
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Ignore outdated entries in the priority queue.
        if current_distance > distances[current_node]:
            continue

        # Visit all the neighbors of the current node and update their distances
        # if a shorter path is found.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Choose a starting node for testing
start_node = 'A'

# Test the dijkstra function
shortest_distances = dijkstra(graph, start_node)
print(shortest_distances)
