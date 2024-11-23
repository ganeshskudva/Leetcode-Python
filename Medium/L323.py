from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Count the number of connected components in an undirected graph.

        :param n: Number of nodes.
        :param edges: List of undirected edges between nodes.
        :return: Number of connected components.
        """
        # Create an adjacency list representation of the graph.
        mp = defaultdict(list)  # Adjacency list
        vis = set()  # Set to track visited nodes
        
        # Build the graph from the edges
        for src, dest in edges:
            mp[src].append(dest)
            mp[dest].append(src)

        # Depth-First Search (DFS) to traverse the graph and mark connected nodes.
        def solve(node):
            if node in vis:
                return  # If the node is already visited, exit
            vis.add(node)  # Mark the node as visited

            # Recursively visit all neighbors of the current node
            for nei in mp[node]:
                solve(nei)

        cnt = 0  # Counter for connected components

        # Iterate through all nodes
        for i in range(n):
            if i not in vis:  # If the node hasn't been visited
                solve(i)  # Perform DFS starting from this node
                cnt += 1  # Increment the connected components count

        return cnt

# Time Complexity (TC):
# - Building the adjacency list: O(e), where 'e' is the number of edges.
# - DFS Traversal: Each node is visited once, and each edge is explored once, leading to O(n + e).
# - Total: O(n + e), where 'n' is the number of nodes and 'e' is the number of edges.

# Space Complexity (SC):
# - Adjacency list: O(n + e), where 'n' nodes and 'e' edges are stored.
# - Visited set: O(n), as we track visited nodes.
# - Recursive stack (DFS): O(n) in the worst case if the graph is a single connected component.
# - Total: O(n + e).
