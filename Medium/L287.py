class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Initialize two pointers, slow and fast
        slow, fast = nums[0], nums[nums[0]]
        
        # Step 2: Detect the cycle using Floyd's Tortoise and Hare algorithm
        while slow != fast:
            slow = nums[slow]           # Move slow pointer one step
            fast = nums[nums[fast]]    # Move fast pointer two steps
        
        # Step 3: Find the entrance to the cycle
        fast = 0  # Reset fast pointer to the start
        while fast != slow:
            fast = nums[fast]  # Move both pointers one step
            slow = nums[slow]
        
        # Step 4: The duplicate number is the entrance to the cycle
        return slow

# Time Complexity (TC):
# 1. Cycle detection:
#    - Both slow and fast pointers traverse the array to detect the cycle.
#    - In the worst case, this step takes O(n), where n is the size of the array.
# 2. Finding the cycle entrance:
#    - Once the cycle is detected, resetting and moving the pointers takes at most O(n) steps.
# Overall TC: O(n).

# Space Complexity (SC):
# 1. The algorithm uses a constant amount of extra space:
#    - Two pointers (`slow` and `fast`).
#    - No additional data structures are used.
# Overall SC: O(1).
