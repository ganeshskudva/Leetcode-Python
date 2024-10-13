class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # Step 1: Create an array 'res' of size 51 to handle ranges between 1 and 50.
        # We use size 51 because we are dealing with indices from 1 to 50.
        res = [0] * 51

        # Step 2: Process each range in 'ranges' by marking the start and end in the 'res' array.
        # For each range [lft, rgt], increment the start position (lft) and decrement the position (rgt + 1).
        for lft, rgt in ranges:
            res[lft] += 1
            if rgt + 1 < len(res):
                res[rgt + 1] -= 1

        # Step 3: Accumulate the count values starting from 'left' to 'right' directly.
        # We only care about numbers from 'left' to 'right', so no need to start from 1.
        overlap = 0
        for i in range(1, right + 1):
            overlap += res[i]
            if i >= left and overlap == 0:
                return False

        # Step 4: If all numbers in the range [left, right] are covered, return True.
        return True

# Time Complexity (TC):
# 1. The loop over 'ranges' to update the 'res' array runs in O(m), where 'm' is the number of ranges.
# 2. The second loop runs from 1 to 'right', which is O(n), where 'n' is the value of 'right'.
# Therefore, the overall time complexity is O(m + n), where 'm' is the number of ranges and 'n' is the value of 'right'.

# Space Complexity (SC):
# 1. The 'res' array takes O(51) = O(1) space.
# 2. Other variables take constant space, so the overall space complexity is O(1).
