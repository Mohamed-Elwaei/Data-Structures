n = 0
adj = []
color = []
parent = []
cycle_start, cycle_end = -1, -1

def dfs(v,color,parent):
    global cycle_start, cycle_end
    color[v] = 1
    for u in adj[v]:
        if color[u] == 0:
            parent[u] = v
            if dfs(u,color,parent):
                return True
        elif color[u] == 1:
            cycle_end = v
            cycle_start = u
            return True
    color[v] = 2
    return False

def find_cycle():
    global cycle_start
    color = [0] * n
    parent = [-1] * n
    cycle_start = -1

    for v in range(n):
        if color[v] == 0 and dfs(v,color,parent):
            break

    if cycle_start == -1:
        print("Acyclic")
    else:
        cycle = []
        cycle.append(cycle_start)
        v = cycle_end
        while v != cycle_start:
            cycle.append(v)
            v = parent[v]
        cycle.append(cycle_start)
        cycle.reverse()

        print("Cycle found:", *cycle)

# Example usage:
n = 5
adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2, 4], [2, 3]]
find_cycle()




n = 6  # Number of vertices
adj = [[] for _ in range(n)]  # Adjacency list representation of the graph

# Add edges to the graph
adj[0].append(1)
adj[1].append(2)
adj[2].append(3)
adj[3].append(4)
adj[4].append(5)
adj[5].append(2)  # Creating a cycle by connecting vertex 5 back to 2

find_cycle()
visited = [False] * n
parent = [-1] * n
cycle_start, cycle_end = -1, -1

def dfs(v, par):
    global cycle_start, cycle_end
    visited[v] = True
    for u in adj[v]:
        if u == par:
            continue
        if visited[u]:
            cycle_end = v
            cycle_start = u
            return True
        parent[u] = v
        if dfs(u, parent[u]):
            return True
    return False

def find_cycle():
    global cycle_start, cycle_end
    visited = [False] * n
    parent = [-1] * n
    cycle_start, cycle_end = -1, -1

    for v in range(n):
        if not visited[v] and dfs(v, parent[v]):
            break

    if cycle_start == -1:
        print("Acyclic")
    else:
        cycle = [cycle_start]
        v = cycle_end
        while v != cycle_start:
            cycle.append(v)
            v = parent[v]
        cycle.append(cycle_start)

        print("Cycle found:", end=" ")
        for v in cycle:
            print(v, end=" ")
        print()

# You can use the translated Python code with appropriate values for 'n' and 'adj'.

n = 6  # Number of vertices
adj = [[] for _ in range(n)]  # Adjacency list representation of the graph

# Add edges to the graph
adj[0].append(1)
adj[1].append(2)
adj[2].append(3)
adj[3].append(4)
adj[4].append(5)
adj[5].append(2)  # Creating a cycle by connecting vertex 5 back to 2

find_cycle()
