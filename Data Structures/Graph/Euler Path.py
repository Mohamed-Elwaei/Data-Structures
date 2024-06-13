def is_eulerian(graph):
    """
    Check if the given graph has an Eulerian path.
    
    Parameters:
        graph (dict): An adjacency list representation of the graph.
                      The keys are nodes, and the values are lists of neighboring nodes.

    Returns:
        bool: True if an Eulerian path exists, False otherwise.
    """
    odd_degree_count = sum(1 for node in graph.values() if len(node) % 2 == 1)

    if odd_degree_count == 0 or odd_degree_count == 2:
        return True
    else:
        return False

def eulerian_path(graph, start_node=None):
    """
    Find an Eulerian path in the given graph.

    Parameters:
        graph (dict): An adjacency list representation of the graph.
                      The keys are nodes, and the values are lists of neighboring nodes.
        start_node: The starting node for the Eulerian path. If not provided, the algorithm
                    will try to find a suitable starting node automatically.

    Returns:
        list or None: The list of nodes forming an Eulerian path if one exists,
                      otherwise returns None.
    """
    def dfs(node):
        while graph[node]:
            neighbor = graph[node].pop()
            dfs(neighbor)
        path.append(node)

    if not is_eulerian(graph):
        return None

    if start_node is None:
        # Find a node with odd degree (if exists) to use as the starting node.
        start_node = next((node for node in graph if len(graph[node]) % 2 == 1), None)
        if start_node is None:
            start_node = next(iter(graph))  # Pick any node as the starting node.

    path = []
    dfs(start_node)

    return path[::-1]

# Example usage:
if __name__ == "__main__":
    # Sample graph represented as an adjacency list
    sample_graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B'],
        'D': ['A', 'B']
    }

    if is_eulerian(sample_graph):
        path = eulerian_path(sample_graph)
        print("Eulerian Path:", path)
    else:
        print("No Eulerian Path exists in the given graph.")
