class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Step 1: Create a graph (adjacency list) to represent the connections.
        # - If a connection goes from 'src' to 'dest', append 'dest' to 'mp[src]'.
        # - We append '-src' to 'mp[dest]' to mark the reverse edge, indicating a road from 'src' to 'dest'.
        #   This helps us know if the current edge needs to be changed (if it needs to be reversed).
        mp = defaultdict(list)
        for src, dest in connections:
            mp[src].append(dest)
            mp[dest].append(-src)

        # Step 2: Recursive DFS function to explore the graph.
        # - It takes 'start' as the current node and a visited set 'vis' to avoid revisiting nodes.
        def solve(start, vis=None):
            change = 0  # Initialize the count of roads that need to be changed.
            if not vis:
                vis = set()  # Initialize visited set if not provided.
            vis.add(start)  # Mark the current node as visited.
            
            # Explore all neighbors (positive or negative) connected to the current node.
            for nei in mp[start]:
                if abs(nei) not in vis:  # If the absolute value of the neighbor hasn't been visited:
                    change += solve(abs(nei), vis)  # Recursively solve for the neighbor.
                    
                    # If the neighbor is positive, it means there is a road from 'start' to 'nei',
                    # which means this road needs to be reversed. Increment the change counter.
                    change += 1 if nei > 0 else 0

            return change  # Return the number of changes needed for the current subtree.

        # Step 3: Start DFS from node 0, since it's the central city (destination city).
        return solve(0)

# Time Complexity (TC):
# - Graph Construction: Building the adjacency list takes O(n) time, where n is the number of cities (nodes).
# - DFS Traversal: The DFS visits each node and processes each edge once. This also takes O(n) time.
# - Overall Time Complexity: O(n), since both graph construction and DFS traversal visit each node and edge once.

# Space Complexity (SC):
# - Adjacency List (mp): Storing the graph requires O(n) space, where n is the number of cities.
# - Visited Set (vis): The visited set stores up to n cities, so its space complexity is O(n).
# - Recursion Stack: The depth of the recursion stack can be up to O(n) in the worst case.
# - Overall Space Complexity: O(n), as space is required for the adjacency list, visited set, and recursion stack.
