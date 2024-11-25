from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Find the number of provinces (connected components) in the isConnected graph.

        Args:
        isConnected (List[List[int]]): Adjacency matrix representing connections between cities.

        Returns:
        int: Number of provinces (connected components).
        """
        n = len(isConnected)  # Number of cities
        visited = set()  # To track visited cities
        provinces = 0  # Number of provinces

        def solve(city):
            """
            Perform DFS to mark all cities connected to the current city.

            Args:
            city (int): The current city being visited.
            """
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)  # Mark as visited
                    solve(neighbor)  # Continue DFS

        # Iterate through each city
        for city in range(n):
            if city not in visited:  # Start a new DFS if the city hasn't been visited
                visited.add(city)  # Mark the city as visited
                solve(city)  # Explore the entire connected component
                provinces += 1  # Increment the province count

        return provinces

# Time Complexity: O(n^2), where n is the number of cities.
#     - We iterate over the matrix during DFS traversal.

# Space Complexity: O(n), where n is the number of cities.
#     - Space is used for the visited set and the recursion stack.
