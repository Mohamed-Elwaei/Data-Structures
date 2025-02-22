def bellman_ford(graph, source):
    # Step 1: Prepare the distance, predecessor, and path for each node
    distance, predecessor, path = dict(), dict(), dict()
    for node in graph:
        distance[node], predecessor[node], path[node] = float('inf'), None, []

    distance[source] = 0
    path[source] = [source]

    # Step 2: Relax the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                new_distance = distance[node] + graph[node][neighbour]
                if new_distance < distance[neighbour]:
                    distance[neighbour] = new_distance
                    predecessor[neighbour] = node
                    path[neighbour] = path[node] + [neighbour]

    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour], "Negative weight cycle."

    return distance, path

    

graph = {
    'a': {'b': -1, 'c':  4},
    'b': {'c':  3, 'd':  2, 'e':  2},
    'c': {},
    'd': {'b':  1, 'c':  5},
    'e': {'d': -3}
}

distance, predecessor = bellman_ford(graph, source='a')

print(distance)
print(predecessor)
graph = {
    'a': {'c': 3},
    'b': {'a': 2},
    'c': {'b': 7, 'd': 1},
    'd': {'a': 6},
}

distance, predecessor = bellman_ford(graph, source='a')

print(distance)
