from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # Initialize the result counter for total friend requests
        res = 0
        # Sort the ages to allow for binary search and range checking
        ages.sort()

        # Helper function to perform binary search and find the upper bound for a target age
        def solve(tgt):
            lo, hi = 0, len(ages) - 1
            # Binary search to find the rightmost index where age is <= tgt
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if ages[mid] <= tgt:
                    lo = mid + 1
                else:
                    hi = mid - 1
            # Return the position of the upper bound (next position after the last valid age)
            return lo

        # Main loop: calculate requests for each age
        for i in range(len(ages)):
            # Calculate the valid lower and upper bounds for sending a friend request
            lower = solve(ages[i] // 2 + 7)  # Minimum age allowed to receive a friend request
            upper = solve(ages[i])  # Maximum age (current age) allowed
            # Calculate requests within the range and exclude the current person themselves
            res += max(upper - lower - 1, 0)

        # Return the total number of friend requests
        return res

# Time Complexity (TC):
# - Sorting ages takes O(N log N), where N is the number of ages.
# - For each age in the list (N elements), we perform two binary searches, each O(log N),
#   resulting in O(N log N) for the binary search portion.
# - Overall time complexity: O(N log N) for sorting + O(N log N) for the binary search,
#   resulting in O(N log N) in total.

# Space Complexity (SC):
# - The space complexity is O(1) additional space, as we only use a few variables and the `solve` function.
# - Sorting is done in place, so no extra space is required for the sorted list.
# - Overall space complexity: O(1).
