## Greedy

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize the number of jumps, the current endpoint we can reach, 
        # and the farthest point we can reach at any point
        jumps, curr_end, curr_farthest = 0, 0, 0
        
        # Iterate through the array (but not the last element since we don't need to jump from there)
        for i in range(len(nums) - 1):
            # Update the farthest point we can reach
            curr_farthest = max(curr_farthest, i + nums[i])
            
            # If we have reached the current endpoint, increment the jump count and update curr_end
            if i == curr_end:
                jumps += 1
                curr_end = curr_farthest
                
                # If the current endpoint is beyond or at the last element, we can stop
                if curr_end >= len(nums) - 1:
                    break
        
        return jumps

# Time Complexity (TC):
# - We only iterate through the `nums` array once (i.e., a single loop), and each index is visited exactly once.
# - Inside the loop, all operations are constant time (O(1)), such as calculating the farthest point and updating variables.
# - Hence, the overall time complexity is O(N), where N is the length of the `nums` array.

# Space Complexity (SC):
# - The algorithm uses a constant amount of extra space (three variables: `jumps`, `curr_end`, and `curr_farthest`).
# - Therefore, the space complexity is O(1), as no additional space is used that scales with the input size.


## DP

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Memoization map to store the minimum jumps needed from each index
        dp = defaultdict(int)

        # Helper function with memoization to calculate the minimum jumps from 'idx' to the last index
        def solve(idx):
            # Base case: If we reach or go beyond the last index, no more jumps are needed
            if idx >= len(nums) - 1:
                return 0
            
            # If we've already computed the result for this index, return it
            if idx in dp:
                return dp[idx]

            # Initialize min_jump to a very large value (infinity)
            min_jump = float('inf')
            
            # Calculate the maximum jump we can make from the current index
            max_jump = min(len(nums), idx + nums[idx])
            
            # Try all possible jumps from the current index
            for i in range(idx + 1, max_jump + 1):
                if i in dp:
                    # If already computed for index 'i', use it
                    min_jump = min(min_jump, 1 + dp[i])
                else:
                    # Recursively compute the minimum jumps for index 'i'
                    min_jump = min(min_jump, 1 + solve(i))

            # Memoize the result for the current index
            dp[idx] = min_jump
            return dp[idx]

        # Start solving from index 0
        return solve(0)

# Time Complexity (TC):
# - In the worst case, each index is visited once and can jump to multiple other indices.
# - The recursion tree has a branching factor limited by the number of jumps, but memoization ensures each index is only solved once.
# - Thus, the time complexity is O(N), where N is the length of the nums array.

# Space Complexity (SC):
# - The space complexity is primarily due to the memoization dictionary `dp` that stores results for each index.
# - In the worst case, we may store results for every index, so space complexity is O(N).
# - Additionally, the recursion stack may use O(N) space in the worst case.
# - Therefore, the total space complexity is O(N).
