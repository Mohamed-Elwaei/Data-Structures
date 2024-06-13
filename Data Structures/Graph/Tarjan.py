UNVISITED = -1

def findSccs(n, g):
    global id, sccCount, ids, low, onStack, stack
    id = 0
    sccCount = 0
    ids = [UNVISITED] * n
    low = [0] * n
    onStack = [False] * n
    stack = []

    for i in range(n):
        if ids[i] == UNVISITED:
            dfs(i, g)

    return low

def dfs(node, g):
    global id, sccCount, ids, low, onStack, stack
    ids[node] = id
    low[node] = id
    id += 1
    stack.append(node)
    onStack[node] = True

    for neighbor in g[node]:
        if ids[neighbor] == UNVISITED:
            dfs(neighbor, g)
        if onStack[neighbor]: 
            low[node] = min(low[node], low[neighbor])

    if ids[node] == low[node]:
        scc_group = []
        while True:
            top = stack.pop()
            onStack[top] = False
            scc_group.append(top)
            if top == node:
                break
        sccCount += 1
        # Process the strongly connected component here (scc_group)

# Example usage:
n = 8
g = [[1], [2], [0, 3], [4], [5, 6], [3], [7], []]

low_values = findSccs(n, g)
print(low_values)
