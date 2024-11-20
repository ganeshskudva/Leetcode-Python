class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_til_now, res = heights[-1], [len(heights) - 1]

        # Traverse from the second-to-last building to the first
        for i in range(len(heights) - 2, -1, -1):
            # If the current building is taller than all to its right, it has an ocean view
            if heights[i] > max_til_now:
                res.append(i)
            # Update the max height seen so far
            max_til_now = max(max_til_now, heights[i])

        # Return indices in ascending order
        return res[::-1]

# Time Complexity (TC): O(n)
# - We traverse the `heights` list once, which takes O(n).
# - Reversing the `res` list also takes O(k), where k is the length of `res`.
# - In the worst case, k = n (all buildings have ocean view).
# - Total time complexity: O(n).

# Space Complexity (SC): O(k)
# - The `res` list stores the indices of buildings with ocean view.
# - In the worst case, all buildings have ocean view, so k = n.
# - Total space complexity: O(n).
