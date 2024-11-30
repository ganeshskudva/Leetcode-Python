# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Finds the first bad version in a sequence of versions 1 to n.

        Time Complexity: O(log n) - Binary search reduces the search space by half at each step.
        Space Complexity: O(1) - Uses constant extra space.
        """
        lo, hi = 1, n

        while lo < hi:
            mid = lo + (hi - lo) // 2  # Avoid potential overflow
            if isBadVersion(mid):
                hi = mid  # Narrow down to the left half
            else:
                lo = mid + 1  # Narrow down to the right half

        return lo  # `lo` is the first bad version

# Time Complexity: O(log n) - Binary search reduces the search space by half at each step.
# Space Complexity: O(1) - Uses constant extra space.