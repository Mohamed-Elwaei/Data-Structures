import heapq

def prim(graph):
    source_node = next(iter(graph))  # Select the first node as the source node
    visited_nodes = {source_node}
    min_heap = []

    # Initialize the min_heap with edges from the source node
    for neighbor, weight in graph[source_node].items():
        heapq.heappush(min_heap, (weight, source_node, neighbor))

    minimum_spanning_tree = []

    while len(visited_nodes) < len(graph):
        weight, u, v = heapq.heappop(min_heap)

        if v not in visited_nodes:
            visited_nodes.add(v)
            minimum_spanning_tree.append((u, v, weight))

            # Add edges from the newly added node to unvisited neighbors in the min_heap
            for neighbor, weight in graph[v].items():
                if neighbor not in visited_nodes:
                    heapq.heappush(min_heap, (weight, v, neighbor))

    return minimum_spanning_tree

# Example usage:
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4, 'D': 1},
    'C': {'A': 3, 'B': 4, 'D': 5},
    'D': {'B': 1, 'C': 5}
}

mst = prim(graph)
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
