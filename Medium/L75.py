class Solution:
    def sortColors(self, nums):
        # Initialize pointers:
        # - red points to the boundary for 0s (red region)
        # - white processes the current element
        # - blue points to the boundary for 2s (blue region)
        red, white, blue = 0, 0, len(nums) - 1

        # Process the array until the white pointer crosses the blue pointer
        while white <= blue:
            if nums[white] == 0:  # Current element is 0 (red)
                # Swap the current element with the red pointer
                nums[red], nums[white] = nums[white], nums[red]
                # Expand both red and white regions
                red += 1
                white += 1
            elif nums[white] == 1:  # Current element is 1 (white)
                # Leave it in place and move the white pointer
                white += 1
            else:  # Current element is 2 (blue)
                # Swap the current element with the blue pointer
                nums[white], nums[blue] = nums[blue], nums[white]
                # Shrink the blue region
                blue -= 1

# Time Complexity (TC):
# 1. The loop runs while `white` <= `blue`, processing each element exactly once.
# 2. Each swap operation takes O(1), and no element is processed more than once.
# 3. Therefore, the total time complexity is O(n), where n is the length of the array.

# Space Complexity (SC):
# 1. The algorithm uses a constant amount of extra space, regardless of the input size.
# 2. Three integer variables (`red`, `white`, `blue`) are used to manage the pointers.
# 3. Sorting is done in place, so no additional space is needed for another data structure.
# 4. Therefore, the total space complexity is O(1).

