from collections import defaultdict, deque

def valid_arrangement(pairs):
    """
    Given pairs representing directed edges, find a valid arrangement where
    each edge follows another.

    Time Complexity: O(V + E), where V is the number of unique vertices and E is the number of edges.
    Space Complexity: O(V + E) for graph and recursion stack.
    """
    def build_graph():
        """Builds the graph and calculates out-degree differences."""
        graph = defaultdict(deque)
        out_degree = defaultdict(int)

        for u, v in pairs:
            graph[u].append(v)
            out_degree[u] += 1
            out_degree[v] -= 1

        return graph, out_degree

    def find_start():
        """Finds the starting node for Eulerian path."""
        for node, degree in out_degree.items():
            if degree == 1:
                return node
        return pairs[0][0]  # Default to any node if no unique start

    def dfs(node):
        """Performs DFS to arrange the path."""
        while graph[node]:
            next_node = graph[node].pop()
            dfs(next_node)
            result.appendleft((node, next_node))

    # Build the graph and determine out-degrees
    graph, out_degree = build_graph()

    # Find the starting node
    start_node = find_start()

    # Result to store the arrangement
    result = deque()

    # Perform DFS
    dfs(start_node)

    return list(result)

# Time Complexity: O(V + E), where V is the number of unique vertices and E is the number of edges.
# Space Complexity: O(V + E) for graph and recursion stack.