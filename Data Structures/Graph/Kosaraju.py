from collections import defaultdict

def transpose(graph):
    g = defaultdict(list)

    for u in graph:
        for v in graph[u]:
            g[v].append(u)
    return g
def dfs(node,stack,visited,graph):
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour,stack,visited,graph)
    stack.append(node)


def kosaraju(graph):
    stack = []
    visited =set()

    for u in graph:
        if u not in visited:
            dfs(u,stack,visited,graph)
        
    gt = transpose(graph)

    visited = set()

    sccs = []
    while stack:
        u = stack.pop()
        if u not in visited:
            scc = []
            dfs(u,scc,visited,gt)
            sccs.append(scc)
    return sccs

    
# Create a sample directed graph as a dictionary of adjacency lists
sample_graph = {
    1: [2,3],
    2: [1,4],
    3: [],
    4: []
}

# Find strongly connected components in the sample graph
sccs = kosaraju(sample_graph)

# Print the strongly connected components
for idx, scc in enumerate(sccs):
    print(f"Strongly Connected Component {idx + 1}: {scc}")

