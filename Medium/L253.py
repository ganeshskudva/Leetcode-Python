class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        hp = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in intervals:
            if hp and i[0] >= hp[0]:
                heapq.heapreplace(hp, i[1])
            else:
                heapq.heappush(hp, i[1])

        return len(hp)
