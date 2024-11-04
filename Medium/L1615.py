from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Initialize a 2D list to track if two cities are directly connected
        # Space Complexity: O(n^2) for the `connected` matrix
        connected = [[False] * n for _ in range(n)]
        
        # Initialize an array to count the number of roads connected to each city
        # Space Complexity: O(n) for the `cnts` list
        cnts = [0] * n
        
        # Populate the `connected` matrix and the `cnts` list
        for r in roads:
            cnts[r[0]] += 1
            cnts[r[1]] += 1
            connected[r[0]][r[1]] = True
            connected[r[1]][r[0]] = True  # Mark as directly connected

        res = 0  # Initialize result to store the maximal network rank
        
        # Iterate over all unique pairs of cities (i, j) with i < j
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the network rank for this pair of cities
                # Subtract 1 if they are directly connected to avoid double-counting
                network_rank = cnts[i] + cnts[j] - (1 if connected[i][j] else 0)
                # Update the result with the maximum network rank found
                res = max(res, network_rank)

        return res

# Overall Time Complexity: O(n^2) for the nested loops, where we check all pairs of cities.
# Overall Space Complexity: O(n^2) for the `connected` matrix and O(n) for the `cnts` list, giving a total of O(n^2).
