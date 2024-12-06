def largestPerimeter(self, nums: List[int]) -> int:
    # Sort the array in descending order to handle the largest sides first
    nums.sort(reverse=True)
    
    # Iterate through the sorted list to find the largest valid triangle
    for i in range(len(nums) - 2):
        # Check the triangle inequality
        if nums[i] < nums[i + 1] + nums[i + 2]:
            # Return the perimeter of the triangle
            return nums[i] + nums[i + 1] + nums[i + 2]
    
    # Return 0 if no valid triangle is found
    return 0

# Time Complexity (TC):
# O(n log n) - Sorting dominates the complexity. The loop is O(n), which is negligible in comparison.

# Space Complexity (SC):
# O(1) - Sorting in place and using a constant amount of extra space.
