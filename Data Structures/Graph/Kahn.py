from collections import defaultdict, deque

def topological_sort(graph):
    # Calculate in-degrees for all nodes in the graph
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Initialize a queue with nodes having in-degrees of 0
    queue = deque([node for node in graph if in_degree[node] == 0])
    
    # Initialize the result list
    topological_order = []

    # Perform Kahn's algorithm
    while queue:
        node = queue.popleft()
        topological_order.append(node)

        # Remove the current node from its neighbors' in-degrees
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the graph is a DAG, the result will contain all nodes; otherwise, there's a cycle.
    if len(topological_order) == len(graph):
        return topological_order
    else:
        return []  # The graph contains a cycle

def kahn(graph):
    ins = {node: 0 for node in graph}
    for u in graph:
        for v in graph[u]:
            ins[v]+=1
    
    queue = deque([node for node in graph if ins[node] == 0])

    order = []
    while queue:
        curr = queue.popleft()
        order.append(curr)

        for v in graph[curr]:
            ins[v] -=1
            if ins[v] == 0:
                queue.append(v)
        
    if len(order) == len(graph):
        return order
    else:
        return 'Cycle Detected'



# Example usage:
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

result = kahn(graph)
if result:
    print("Topological Order:", result)
else:
    print("The graph contains a cycle.")
