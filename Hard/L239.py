class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []

        n = len(nums)
        if k == 1:
            return nums

        dq = deque()  # Stores indices of elements in the window
        result = []

        for right in range(n):
            # Remove indices of elements not in the sliding window
            while dq and dq[0] < right - k + 1:
                dq.popleft()

            # Remove indices of elements smaller than the current element
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # Add the current index to the deque
            dq.append(right)

            # Append the maximum of the current window to the result
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result

# Time Complexity (TC):
# - Each element is added to the deque once and removed from the deque at most once.
# - The total operations related to adding and removing elements from the deque are O(n).
# - Therefore, the time complexity is O(n).

# Space Complexity (SC):
# - The deque stores at most 'w' indices, where 'w' is the size of the sliding window.
# - The result list stores (n - w + 1) elements, but this is required output and not considered additional space usage.
# - Therefore, the auxiliary space complexity is O(w).