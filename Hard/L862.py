from collections import deque

class Solution:
    def shortestSubarray(self, nums, k):
        """
        Find the length of the shortest subarray with a sum >= k.

        Args:
        nums (List[int]): Array of integers.
        k (int): Target sum.

        Returns:
        int: Length of the shortest subarray, or -1 if no such subarray exists.

        Time Complexity:
        O(n): Each index is added to and removed from the deque exactly once.
        
        Space Complexity:
        O(n): For the prefix_sum array and deque storage.
        """

        n_len = len(nums)
        shortest = n_len + 1  # Initialize to a value larger than the possible maximum

        # Building a prefix/cumulative sum of all elements
        prefix_sum = [0] * (n_len + 1)
        for i in range(n_len):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # Initialize the deque for storing the starting indices
        start_idxs = deque()

        for i in range(n_len + 1):
            # Find the smallest window whose sum >= k
            while start_idxs and prefix_sum[i] - prefix_sum[start_idxs[0]] >= k:
                # Update the shortest length if a valid subarray is found
                shortest = min(shortest, i - start_idxs.popleft())

            # Maintain deque in increasing order of prefix_sum
            while start_idxs and prefix_sum[i] <= prefix_sum[start_idxs[-1]]:
                start_idxs.pop()

            # Add the current index to the deque
            start_idxs.append(i)

        # Return the result; -1 if no valid subarray was found
        return shortest if shortest <= n_len else -1

# Time Complexity: O(n)
# Each index is added to and removed from the deque exactly once. The prefix sum calculation is O(n), so the overall complexity is linear.

# Space Complexity: O(n)
# The prefix_sum array requires O(n) space, and the deque also requires O(n) space in the worst case.
