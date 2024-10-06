class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Step 1: Initialize variables.
        # 'n' is the number of bombs.
        # 'ans' will store the maximum number of bombs detonated.
        # 'mp' is a dictionary where each bomb (key) has a list of other bombs (values) that can be detonated by it.
        n, ans, mp = len(bombs), 0, defaultdict(list)

        # Step 2: Helper function to determine if bomb at (x2, y2) is within the blast radius of bomb at (x1, y1) with radius r.
        # Uses the Euclidean distance formula: r^2 >= (x1 - x2)^2 + (y1 - y2)^2 to check if a bomb is within range.
        def is_within_range(x1, y1, x2, y2, r):
            return r ** 2 >= (x1 - x2) ** 2 + (y1 - y2) ** 2

        # Step 3: Build the adjacency list.
        # For each pair of bombs (i, j), if bomb j is within the blast radius of bomb i, add bomb j to bomb i's list.
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue  # Skip if the bombs are the same.
                # Check if bomb j is within the blast radius of bomb i.
                if is_within_range(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1], bombs[i][2]):
                    mp[i].append(j)

        # Step 4: DFS to traverse and count how many bombs can be detonated starting from 'node'.
        def dfs(node, visited):
            # For each neighboring bomb that can be detonated, recursively explore if it can detonate more bombs.
            for child in mp[node]:
                if child not in visited:
                    visited.add(child)  # Mark as visited.
                    dfs(child, visited)

        # Step 5: Try detonating bombs starting from each bomb and use DFS to find how many bombs can be detonated.
        for i in range(n):
            vis = {i}  # Set to track visited bombs, starting with bomb i.
            dfs(i, vis)  # Run DFS to explore all reachable bombs from bomb i.
            ans = max(ans, len(vis))  # Update the maximum number of bombs detonated.

        # Step 6: Return the maximum number of bombs that can be detonated from a single initial bomb.
        return ans

# Time Complexity (TC):
# - Building the adjacency list: We compare each pair of bombs (i, j), which takes O(n^2) time, where n is the number of bombs.
# - DFS traversal: In the worst case, we explore all bombs starting from each bomb, which takes O(n + e) for each DFS call,
#   where e is the number of edges in the graph (i.e., detonable bomb connections). In the worst case, this could be O(n^2) as well.
# - The overall time complexity is O(n^2) for building the graph and exploring all bombs using DFS.

# Space Complexity (SC):
# - The adjacency list 'mp' takes O(n^2) space in the worst case if every bomb can detonate every other bomb.
# - The visited set in each DFS call can hold up to O(n) bombs.
# - The recursion stack for DFS can go as deep as O(n) in the worst case.
# - Overall, the space complexity is O(n^2) due to the adjacency list and the DFS recursion stack.

