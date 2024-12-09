# Optimized
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            # If the height array is empty, no water can be trapped
            return 0

        # Initialize two pointers:
        # `left` starts from the beginning, `right` starts from the end
        left, right = 0, len(height) - 1

        # Variables to keep track of the maximum heights encountered so far from both ends
        left_max, right_max = 0, 0

        # Variable to store the total amount of trapped water
        total_water = 0

        # Iterate until the two pointers meet
        while left < right:
            if height[left] < height[right]:
                # If the left height is less than the right height, process the left side
                if height[left] >= left_max:
                    # Update left_max if the current height is greater or equal
                    left_max = height[left]
                else:
                    # Add trapped water for the current position
                    # Water trapped is the difference between left_max and the current height
                    total_water += left_max - height[left]
                # Move the left pointer to the right
                left += 1
            else:
                # If the right height is less than or equal to the left height, process the right side
                if height[right] >= right_max:
                    # Update right_max if the current height is greater or equal
                    right_max = height[right]
                else:
                    # Add trapped water for the current position
                    # Water trapped is the difference between right_max and the current height
                    total_water += right_max - height[right]
                # Move the right pointer to the left
                right -= 1

        # Return the total amount of trapped water
        return total_water

# Time Complexity (TC):
# 1. The array is traversed once using the two-pointer approach, where each pointer moves inward until they meet.
#    - This results in a time complexity of O(n), where `n` is the length of the input array `height`.
# Overall Time Complexity: O(n).

# Space Complexity (SC):
# 1. The solution uses only a constant amount of extra space for variables (`left`, `right`, `left_max`, `right_max`, `total_water`).
#    - No additional data structures are used.
# Overall Space Complexity: O(1).


# uses more space
class Solution:
    def trap(self, height: List[int]) -> int:
        # If the input list is empty, no water can be trapped
        if len(height) == 0:
            return 0

        # Helper function to calculate the left boundary for each position
        def left_bound():
            # Initialize the left boundary array with zeros
            ret = [0] * len(height)
            # The left boundary at the first index is the height of the first element
            ret[0] = height[0]
            # Compute the left boundary for the rest of the indices
            for i in range(1, len(height)):
                # The left boundary at index i is the maximum of the left boundary at index i-1 and the height at index i
                ret[i] = max(ret[i - 1], height[i])
            return ret

        # Helper function to calculate the right boundary for each position
        def right_bound():
            # Initialize the right boundary array with zeros
            ret = [0] * len(height)
            # The right boundary at the last index is the height of the last element
            ret[-1] = height[-1]
            # Compute the right boundary for the rest of the indices
            for i in range(len(height) - 2, -1, -1):
                # The right boundary at index i is the maximum of the right boundary at index i+1 and the height at index i
                ret[i] = max(ret[i + 1], height[i])
            return ret

        # Compute the left and right boundaries
        left, right, tot = left_bound(), right_bound(), 0
        # Calculate the water trapped at each index
        for i in range(len(height)):
            # Water trapped at index i is the minimum of the left and right boundaries minus the height at index i
            tot += (min(left[i], right[i]) - height[i])

        # Return the total amount of water trapped
        return tot

# Time Complexity (TC):
# 1. Computing the left boundary array:
#    - This involves a single traversal of the `height` array, which takes O(n) time.
# 2. Computing the right boundary array:
#    - Similar to the left boundary, this also takes O(n) time.
# 3. Calculating the total trapped water:
#    - This involves another traversal of the `height` array, which takes O(n) time.
# Overall Time Complexity: O(n), where `n` is the length of the `height` array.

# Space Complexity (SC):
# 1. The left boundary array:
#    - This requires O(n) space.
# 2. The right boundary array:
#    - This also requires O(n) space.
# 3. Additional variables (tot, ret in functions):
#    - These require O(1) space.
# Overall Space Complexity: O(n), due to the storage of the left and right boundary arrays.

        
