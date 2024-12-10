class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Set to keep track of visited nodes to avoid re-visiting
        seen = set()
        # Graph representation using adjacency list
        graph = defaultdict(list)

        # Construct the graph from edges
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        # Recursive DFS function to calculate the minimum time
        def solve(root, cost):
            if root in seen:  # Skip already visited nodes
                return 0

            seen.add(root)  # Mark the current node as visited
            childCost = 0

            # Recursively visit all children of the current node
            for c in graph[root]:
                childCost += solve(c, 2)  # Add the traversal cost (2) for each child

            # If no child has apples and the current node does not have an apple, skip this branch
            if childCost == 0 and not hasApple[root]:
                return 0

            # Add the cost to reach this node if it is part of the path to an apple
            return childCost + cost

        # Start DFS from the root (node 0) with an initial cost of 0
        return solve(0, 0)

# Time Complexity (TC):
# 1. Building the graph: O(n), where n is the number of edges.
# 2. DFS traversal: Each node and edge is visited once in the worst case, resulting in O(n) traversal.
# Overall TC: **O(n)**.

# Space Complexity (SC):
# 1. Graph storage: O(n) for the adjacency list.
# 2. Recursion stack: O(n) in the worst case (if the graph is a single path).
# 3. Seen set: O(n) to store visited nodes.
# Overall SC: **O(n)**.
