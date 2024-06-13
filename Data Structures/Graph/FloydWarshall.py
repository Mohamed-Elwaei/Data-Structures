# Let dist be a |V| * |V| array of minimum distances initialized to Infinity
# Let next be a |V| * |V| array of vertex indices initialized to None

def floyd_warshall_with_path_reconstruction(dist, next):
    V = len(dist)

    for u in range(V):
        for v in range(V):
            dist[u][v] = w(u, v)  # The weight of the edge (u, v)
            next[u][v] = v

    for v in range(V):
        dist[v][v] = 0
        next[v][v] = v

    for k in range(V):  # standard Floyd-Warshall implementation
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]

def path(u, v, next):
    if next[u][v] is None:
        return []

    path_result = [u]
    while u != v:
        u = next[u][v]
        path_result.append(u)

    return path_result
# Example graph with weights
#     0    1    2    3
# 0  0   2∞    3    4
# 1  1    0    2∞   5
# 2  3    2    0    1
# 3  6    5    1    0

V = 4  # Number of vertices

# Initialize dist array with Infinity
dist = [[float('inf')] * V for _ in range(V)]

# Initialize next array with None
next = [[None] * V for _ in range(V)]

# Example weights for the edges
weights = [
    [0, float('inf'), 3, 4],
    [1, 0, float('inf'), 5],
    [3, 2, 0, 1],
    [6, 5, 1, 0]
]

# Assign weights to the graph
for i in range(V):
    for j in range(V):
        dist[i][j] = weights[i][j]
        next[i][j] = j

# Run Floyd-Warshall algorithm
floyd_warshall_with_path_reconstruction(dist, next)

# Example path reconstruction
source_vertex = 0
destination_vertex = 3

# Find and print the shortest path from source to destination
shortest_path = path(source_vertex, destination_vertex, next)
print(f"Shortest path from {source_vertex} to {destination_vertex}: {shortest_path}")
