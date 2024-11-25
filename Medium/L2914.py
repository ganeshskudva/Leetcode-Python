class Solution:
    def minChanges(self, s: str) -> int:
        """
        Calculate the minimum number of changes required to make
        all pairs of adjacent characters in the string equal.

        Args:
        s (str): The input string.

        Returns:
        int: The number of changes required.

        Time Complexity: O(n), where n is the length of the string.
            - The loop iterates through half of the string's characters (step size = 2).
        
        Space Complexity: O(1).
            - The space usage is constant, as no additional data structures are used.
        """
        # Iterate through the string with a step of 2
        # Count the number of positions where adjacent characters differ
        return sum(1 for i in range(0, len(s) - 1, 2) if s[i] != s[i + 1])

# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(1), as no additional data structures are used.
