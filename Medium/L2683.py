class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
        Determine if a valid original array exists for the given derived array.
        """
        # Try both possible values for the first element (0 and 1)
        for first in [0, 1]:
            original = first  # Assume the first element of the original array
            # Traverse the derived array except the last element
            for result in derived[:-1]:
                original ^= result  # Reverse the XOR operation to find the next original element
            # Check if the validity condition is satisfied for the last element
            if original ^ first == derived[-1]:
                return True
        # If neither assumption for the first element works, return False
        return False

# Time Complexity (TC): O(n)
# - The outer loop runs twice (for `first = 0` and `first = 1`).
# - The inner loop traverses `derived[:-1]` (length n-1) each time.
# - Overall complexity: O(n).

# Space Complexity (SC): O(1)
# - The algorithm uses only a constant amount of extra space.
