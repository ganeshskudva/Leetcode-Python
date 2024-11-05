from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort intervals by start time (default behavior)
        intervals.sort()

        # Compare each interval's start time with the previous interval's end time
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:  # Overlap detected
                return False

        return True

# Time Complexity (TC): O(n log n)
#   - Sorting the intervals by start time takes O(n log n).
#   - The subsequent single pass to check for overlaps is O(n).
#   - Thus, the overall time complexity is dominated by the sort operation, making it O(n log n).

# Space Complexity (SC): O(1)
#   - Sorting is done in-place, and only a constant amount of extra space is used for comparisons.
#   - Therefore, the space complexity is O(1).
