class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers and a variable to store the maximum area
        left, right, mx_area = 0, len(height) - 1, 0
        
        # Iterate while the left pointer is less than the right pointer
        while left < right:
            # Calculate the area between the two pointers
            # Area = width * min(height of left, height of right)
            mx_area = max(mx_area, (right - left) * min(height[left], height[right]))
            
            # Move the pointer that has the shorter height
            # This helps in maximizing the area by possibly finding a taller boundary
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        # Return the maximum area found
        return mx_area

# Overall Time Complexity (TC): O(n), where n is the number of elements in height
# This is because each pointer (left and right) moves at most once from start to end.

# Overall Space Complexity (SC): O(1), as we are using a constant amount of space
# for the pointers and the maximum area variable.
