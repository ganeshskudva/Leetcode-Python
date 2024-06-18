class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        start, end, cnt = -1, -1, 0

        for curr_start, curr_end in intervals:
            if start < curr_start and end < curr_end:
                start, cnt = curr_start, cnt + 1
            end = max(end, curr_end)

        return cnt
