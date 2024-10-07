from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # mp: Adjacency list representing the graph where each node has a list of its neighbors
        # vis: A set to track visited nodes during the DFS traversal
        mp, vis = defaultdict(list), set()

        # Step 1: A valid tree must have exactly n-1 edges (n nodes, n-1 edges)
        # If the number of edges is not exactly n-1, it's impossible to form a valid tree.
        # Time Complexity: O(1), as checking the length of the edges and comparing it to n-1 takes constant time.
        # Space Complexity: O(1)
        if len(edges) != n - 1:
            return False  # If the number of edges is not equal to n-1, it's not a valid tree.

        # Step 2: Build the adjacency list (graph) representation from the edge list
        # Time Complexity: O(E), where E is the number of edges, because we iterate through all edges to build the graph.
        # Space Complexity: O(V + E), where V is the number of nodes and E is the number of edges. We store the adjacency list which includes each node and its neighbors.
        for src, dest in edges:
            mp[src].append(dest)  # Add a directed edge src -> dest
            mp[dest].append(src)  # Since it's an undirected graph, also add dest -> src

        # Step 3: Depth First Search (DFS) traversal function
        # This function recursively visits all nodes connected to the current node.
        # Time Complexity: O(V + E), where V is the number of nodes and E is the number of edges. Each node and each edge is processed once.
        # Space Complexity: O(V) for the recursion stack and the visited set 'vis', where V is the number of nodes.
        def solve(node=0):
            if node in vis:  # If the node is already visited, return
                return
            vis.add(node)  # Mark the current node as visited
            for nei in mp[node]:  # Visit all the neighbors of the current node
                solve(nei)  # Recursively visit the neighbor nodes

        # Step 4: Start DFS from node 0 (assuming the graph is connected and node 0 exists)
        # Time Complexity: O(V + E), as the DFS will visit each node and edge exactly once.
        # Space Complexity: O(V) for the recursion stack and visited nodes set.
        solve()

        # Step 5: Return True if all nodes were visited exactly once, meaning it's a connected and acyclic graph.
        # Time Complexity: O(1), as we are just comparing the size of the visited set to n.
        # Space Complexity: O(1)
        return len(vis) == n  # If we've visited all n nodes, it's a valid tree.
