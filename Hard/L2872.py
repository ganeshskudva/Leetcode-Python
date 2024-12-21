from collections import defaultdict, deque

class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k) -> int:
        if n <= 1:  # Handle edge case of one or no nodes
            return 1

        count = 0

        # Build adjacency map using defaultdict
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Initialize deque with all leaf nodes (nodes with one connection)
        queue = deque(node for node, neighbors in graph.items() if len(neighbors) == 1)

        # Process leaves layer by layer
        while queue:
            node = queue.popleft()

            # If the node has a parent, retrieve it and remove the node from its neighbors
            if graph[node]:
                parent = graph[node].pop()
                graph[parent].remove(node)

                # Check divisibility and update parent value if needed
                if values[node] % k == 0:
                    count += 1  # Node forms its own component
                else:
                    values[parent] += values[node]  # Merge value into the parent

                # If the parent becomes a leaf, add it to the queue
                if len(graph[parent]) == 1:
                    queue.append(parent)

        # The remaining node in the graph forms a component if its value is divisible by k
        return count + (values[0] % k == 0)

# Time Complexity (TC):
# - Constructing the adjacency list: O(E), where E is the number of edges.
# - BFS traversal of nodes and edges: O(V + E), where V is the number of nodes.
# Overall: O(V + E).

# Space Complexity (SC):
# - Adjacency list storage: O(V + E).
# - Queue for BFS: O(V) in the worst case.
# - Values array: O(V).
# Overall: O(V + E).
