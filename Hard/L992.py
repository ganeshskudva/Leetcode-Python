from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        This function calculates the number of subarrays in `nums` that contain exactly `k` distinct integers.
        It uses the sliding window technique and a helper function to compute the number of subarrays with 
        at most `k` distinct integers. The result is the difference between subarrays with at most `k` and 
        subarrays with at most `k-1` distinct integers.

        Parameters:
        nums (List[int]): A list of integers.
        k (int): The target number of distinct integers in the subarrays.

        Returns:
        int: The number of subarrays that contain exactly `k` distinct integers.

        Time Complexity: O(n), where `n` is the length of the input array `nums`. We traverse the array twice 
                         (once for `at_most(k)` and once for `at_most(k-1)`), so the total complexity is linear.

        Space Complexity: O(n), where `n` is the number of distinct elements in `nums`. This is due to the dictionary 
                          `cnt` used to store the frequency of elements in the sliding window, which can contain 
                          up to `n` unique elements.
        """

        def at_most(count):
            """
            This helper function calculates the number of subarrays with at most `count` distinct integers.

            Parameters:
            count (int): The maximum number of distinct integers allowed in the subarrays.

            Returns:
            int: The number of subarrays that contain at most `count` distinct integers.

            Time Complexity: O(n), where `n` is the length of the input array `nums`. We traverse the array once,
                             and each element is processed at most twice (once when expanding the window and 
                             once when shrinking it).

            Space Complexity: O(n), where `n` is the number of distinct elements in `nums`. The dictionary `cnt` 
                              tracks the frequency of elements in the current sliding window.
            """
            # `cnt` is a dictionary to store the frequency of elements in the sliding window.
            cnt = defaultdict(int)
            
            # Initialize the left boundary of the sliding window and the result variable.
            left, res = 0, 0

            # Traverse the array using `right` as the right boundary of the sliding window.
            for right in range(len(nums)):
                cnt[nums[right]] += 1  # Add the current element `nums[right]` to the window.
                
                # If the current element appears for the first time, reduce the allowed number of distinct elements.
                if cnt[nums[right]] == 1:
                    count -= 1

                # Shrink the window from the left if we have more than the allowed number of distinct elements.
                while count < 0:
                    cnt[nums[left]] -= 1  # Remove `nums[left]` from the window.
                    
                    # If the count of an element goes to 0, it means it's no longer in the window.
                    if cnt[nums[left]] == 0:
                        count += 1  # Increase the allowed distinct count since one element is removed.

                    left += 1  # Move the left boundary to the right to shrink the window.

                # The number of valid subarrays ending at `right` is the size of the current window (`right - left + 1`).
                res += (right - left + 1)

            return res

        # The number of subarrays with exactly `k` distinct integers is the difference between:
        # 1. Subarrays with at most `k` distinct integers.
        # 2. Subarrays with at most `k-1` distinct integers.
        return at_most(k) - at_most(k - 1)
