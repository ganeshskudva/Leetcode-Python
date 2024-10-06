class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Step 1: Create a dictionary 'mp' to map the original node's value to the new cloned node.
        # This helps in avoiding duplication and solving the problem of cycles in the graph.
        mp = {}

        # Step 2: Recursive DFS function to clone the graph.
        def solve(node):
            # Base case: If the current node is None (empty graph or end of recursion), return None.
            if not node:
                return None

            # Step 3: If the node has already been cloned (i.e., its value is in the map),
            # return the cloned node to avoid duplication and handle cycles.
            if node.val in mp:
                return mp[node.val]

            # Step 4: Create a new clone of the current node (but without neighbors yet).
            new_node = Node(node.val)

            # Step 5: Add this new node to the map to mark it as cloned.
            mp[new_node.val] = new_node

            # Step 6: Recursively clone all the neighbors of the current node.
            # For each neighbor of the original node, perform a DFS and add the cloned neighbor to the new node's neighbors list.
            for neigh in node.neighbors:
                new_node.neighbors.append(solve(neigh))

            # Step 7: Return the fully cloned node.
            return new_node

        # Step 8: Start the DFS from the input node and return the cloned graph.
        return solve(node)

# Time Complexity (TC):
# - Each node is visited exactly once during the DFS.
# - For each node, we clone its neighbors, and the total number of edges we traverse is equal to the number of edges in the graph.
# - Hence, the time complexity is O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.

# Space Complexity (SC):
# - The 'mp' dictionary stores the cloned version of each node. In the worst case, all nodes will be cloned, so the space complexity for 'mp' is O(V).
# - The recursion stack for the DFS can go as deep as the number of nodes, which requires O(V) space.
# - Therefore, the overall space complexity is O(V), where V is the number of nodes in the graph.
