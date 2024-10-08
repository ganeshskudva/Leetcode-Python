## Greedy

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the maximum index we can reach from the starting point
        mx = nums[0]
        
        # Iterate through the array starting from index 1
        for i in range(1, len(nums)):
            # If the maximum index we can reach is less than the current index, return False
            if mx < i:
                return False
            
            # Update the maximum index we can reach by jumping from the current index
            mx = max(mx, i + nums[i])
        
        # If we have passed through the loop, it means we can reach the last index, so return True
        return True

# Time Complexity (TC):
# - The loop iterates through the list exactly once, updating the maximum reachable index.
# - Therefore, the time complexity is O(N), where N is the length of the nums array.

# Space Complexity (SC):
# - The algorithm uses a constant amount of extra space, i.e., the variable 'mx' for storing the maximum reachable index.
# - No additional data structures are used that depend on the input size.
# - Therefore, the space complexity is O(1).

## DP

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Memoization map to store if we can jump from a specific index
        mp = defaultdict(bool)

        # Helper function with memoization to check if we can reach the end starting from 'idx'
        def solve(idx=0):
            # Base case: If the index is at or beyond the last index, return True
            if idx >= len(nums) - 1:
                return True
            
            # If the current index has a value of 0, we can't move further from here
            if nums[idx] == 0:
                mp[idx] = False
                return mp[idx]

            # If we've already computed the result for this index, return it
            if idx in mp:
                return mp[idx]

            # Calculate the maximum jump we can make from this index
            max_jump = min(len(nums) - 1, idx + nums[idx])
            
            # Try all possible jumps from the current index
            for i in range(idx + 1, max_jump + 1):
                # If jumping to index 'i' is successful, mark the current index as reachable
                if i not in mp and solve(i):
                    mp[idx] = True
                    return mp[idx]

            # If none of the jumps work, mark the current index as not reachable
            mp[idx] = False
            return mp[idx]

        # Start solving from index 0
        return solve()

# Time Complexity (TC):
# - The recursion can visit each index at most once because we memoize the result for each index.
# - For each index, we perform a loop to try all possible jumps from that index.
# - In the worst case, for each index, we make up to 'nums[i]' recursive calls, which means the overall complexity is O(N^2), where N is the length of the nums array.
#   However, the memoization reduces the need for redundant calculations.
# - Worst-case time complexity: O(N^2), but with memoization, this could be closer to O(N) in practical scenarios.

# Space Complexity (SC):
# - The space complexity is driven by:
#   1. The recursion stack, which can be at most O(N) deep.
#   2. The memoization map 'mp' which stores results for each index, contributing O(N) additional space.
# - Therefore, the overall space complexity is O(N) due to the recursion and memoization map.

