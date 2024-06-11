class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end, lst = newInterval[0], newInterval[1], []

        for itvl in intervals:
            curStart, curEnd = itvl[0], itvl[1]

            if curEnd < start:
                lst.append([curStart, curEnd])
            elif curStart > end:
                lst.append([start, end])
                start, end = curStart, curEnd
            else:
                start = min(start, curStart)
                end = max(end, curEnd)
        lst.append([start, end])

        return lst
