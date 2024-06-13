import collections

def Tarjan(graph):
    V = len(graph)
    current_id = 0
    SCCs = []
    scc_count = 0
    stack, lows, ids = [], collections.defaultdict(lambda: -1), collections.defaultdict(lambda: -1)
    Onstack = collections.defaultdict(lambda: False)

    def DFS(graph, v):
        nonlocal current_id, scc_count
        ids[v] = lows[v] = current_id
        current_id += 1
        stack.append(v)
        Onstack[v] = True

        for neighbour in graph[v]:
            if ids[neighbour] == -1:
                DFS(graph, neighbour)
            if Onstack[neighbour]:
                lows[v] = min(lows[v], lows[neighbour])  # Update lows with neighbour's id, not lows[neighbour]

        if ids[v] == lows[v]:
            scc = []
            while stack:
                top = stack.pop()
                Onstack[top] = False
                scc.append(top)
            if scc:
                scc_count += 1
                SCCs.append(scc)

    for v in graph:
        if ids[v] == -1:
            DFS(graph, v)

    return SCCs, scc_count

# Example graph represented as an adjacency list
graph = {
    0: [1],
    1: [0],
    2: [1, 2, 3],
    3: [2],
    4: [1, 3, 5],
    5: [3, 6],
    6: []
}

# Run Tarjan's algorithm
SCCs, scc_count = Tarjan(graph)

# Print the result
print("Number of strongly connected components:", scc_count)
print("Strongly connected components:")
for scc in SCCs:
    print(scc)
