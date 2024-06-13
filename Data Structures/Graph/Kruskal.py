import collections

def kruskal(graph):
    edges = []

    for u in graph:
        for v, w in graph[u].items():
            edges.append((u, v, w))

    parents = [i for i in range(len(graph.keys()))]

    edges.sort(key= lambda edge: edge[2])
    def find(a):
        if a == parents[a]:
            return a
        else:
            parents[a] = find(parents[a])  # Properly update the parent
            return parents[a]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            parents[a] = b

    A = collections.defaultdict(dict)
    cost=0
    for u, v, w in edges:
        if find(u) != find(v):
            A[u][v] = w
            A[v][u] = w  # Since it's an undirected graph
            union(u, v)
            cost+=w

    return A,cost

# Example graph represented as an adjacency list
graph = {
    0: {1: 10, 2: 6, 3: 5},
    1: {0: 10, 3: 15},
    2: {0: 6, 3: 4},
    3: {0: 5, 1: 15, 2: 4}
}

# Applying Kruskal's algorithm to find the MST
minimum_spanning_tree,cost = kruskal(graph)

# Print the Minimum Spanning Tree
print("Minimum Spanning Tree:")
for u in minimum_spanning_tree:
    for v, w in minimum_spanning_tree[u].items():
        if u < v:  # Print each edge only once (u < v ensures we print each edge only once)
            print(f"Edge: {u} -- {v}, Weight: {w}")

print("Cost is ", cost)