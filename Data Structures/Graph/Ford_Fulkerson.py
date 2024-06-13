from collections import defaultdict, deque


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.num_vertices = len(graph)

    def bfs(self, source, sink, parent):
        visited = [False] * self.num_vertices
        queue = []
        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == sink:
                        return True

        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.num_vertices
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow




def ford_fulkerson(matrix, source, sink):
    V=len(graph)
    parents=[-1]*V
    max_flow=0


    while BFS(matrix, source, sink, parents):
        path_flow=float('inf')

        v=sink
        while v!=source:
            u=parents[v]
            path_flow=min(path_flow, matrix[u][v])
            v=parents[v]
        
        max_flow+=path_flow
        v=sink
        while v!=source:
            u=parents[v]
            matrix[u][v]-=path_flow
            matrix[v][u]+=path_flow
            v=parents[v]
    return max_flow


def BFS(matrix, source, sink, parents):
    visited=set([source])
    queue=deque([source])

    while queue:
        u=queue.popleft()

        for v, cap in enumerate(graph[u]):
            if v not in visited and cap>0:
                visited.add(v)
                parents[v]=u
                queue.append(v)
                if v==sink:
                    return True
    return False



# Example usage:
graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)
source = 0
sink = 5
max_flow = ford_fulkerson(graph,source, sink)
print("Max Flow:", max_flow)
