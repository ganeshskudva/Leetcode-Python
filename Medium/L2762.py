class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l, res = 0, 0
        minD, maxD = deque(), deque()

        for r in range(len(nums)):
            # Maintain the monotonic property of minD (increasing order)
            while minD and nums[minD[-1]] >= nums[r]:
                minD.pop()
            # Maintain the monotonic property of maxD (decreasing order)
            while maxD and nums[maxD[-1]] <= nums[r]:
                maxD.pop()
            
            # Add the current index to both deques
            minD.append(r)
            maxD.append(r)

            # Ensure the difference condition nums[maxD[0]] - nums[minD[0]] <= 2
            while nums[maxD[0]] - nums[minD[0]] > 2:
                # Increment the left pointer to shrink the window
                l += 1
                # Remove indices that fall out of bounds
                if minD[0] < l:
                    minD.popleft()
                if maxD[0] < l:
                    maxD.popleft()

            # Count all valid subarrays ending at 'r'
            res += r - l + 1

        return res

# Time Complexity (TC):
# The outer loop runs once for each element in the array, O(n).
# Deques ensure each index is added and removed at most once, O(n) for all deque operations.
# Overall TC = O(n).

# Space Complexity (SC):
# The deques store indices for the current window. In the worst case, the window size is proportional to the input size, but deque operations are bounded to O(1) for this problem.
# Overall SC = O(1) (excluding the input array).
