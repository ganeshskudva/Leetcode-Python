class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(list(zip(startTime, endTime, profit)))
        pq = []
        total = 0

        for s, e, p in jobs:
            while pq and pq[0][0] <= s:
                end, pro = heapq.heappop(pq)
                total = max(total, pro)
            heapq.heappush(pq, (e, p + total))

        while pq:
            end, pro = heapq.heappop(pq)
            total = max(total, pro)

        return total