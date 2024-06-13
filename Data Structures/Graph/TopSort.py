def DFS(v, graph, ans, visited):
    visited.add(v)

    for u in graph[v]:
        if u not in visited:
            DFS(u, graph, ans, visited)

    ans.append(v)

def TopSort(graph):
    visited = set()
    ans = []

    for v in graph.keys():
        if v not in visited:  # Check if the vertex has been visited before calling DFS
            DFS(v, graph, ans, visited)

    return ans[::-1]

# Example usage:
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [4],
    4: []
}

result = TopSort(graph)
print(result)  # Output: [0, 1, 2, 3, 4]
