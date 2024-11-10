from typing import List
import sys

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = sys.maxsize

        # Initialize cumulative bit count table with dimensions (n+1) x 32
        self.bitts = [[0] * 32 for _ in range(n + 1)]
        
        # Fill cumulative bit counts for each bit position across all numbers in nums
        for i in range(n):
            for j in range(32):
                self.bitts[i + 1][j] = self.bitts[i][j] + ((nums[i] >> j) & 1)

        # Closure to find the minimum subarray length starting from a given index `idx`
        def answer(idx: int) -> int:
            left, right, local_ans = idx, n - 1, sys.maxsize
            while left <= right:
                mid = (left + right) // 2
                # Calculate the bitwise OR for subarray nums[idx:mid + 1] using cumulative bit counts
                a = 0
                for i in range(32):
                    b = self.bitts[mid + 1][i] - self.bitts[idx][i]
                    if b:
                        a += (1 << i)  # Reconstruct number based on bits

                # Check if this OR value meets or exceeds k
                if a >= k:
                    local_ans = min(local_ans, mid - idx + 1)
                    right = mid - 1  # Try to find a shorter valid subarray
                else:
                    left = mid + 1
            return local_ans

        # Iterate through nums to find minimum subarray length starting at each index
        for i in range(n):
            temp = answer(i)
            if temp != sys.maxsize:
                ans = min(ans, temp)
            else:
                break

        return -1 if ans == sys.maxsize else ans

# Time Complexity (TC): O(n * log(n) * 32)
# - Constructing the cumulative bit count table takes O(n * 32), where 32 is the number of bits in an integer.
# - For each starting index in nums, we use binary search to find the shortest subarray that meets the condition,
#   which takes O(log(n) * 32) per call due to 32-bit processing within the binary search.
# - This results in an overall time complexity of O(n * log(n) * 32).

# Space Complexity (SC): O(n * 32)
# - The cumulative bit count table `bitts` requires O(n * 32) space.
# - Additional space usage is minimal (constant).
