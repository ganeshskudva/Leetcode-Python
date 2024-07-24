class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        n, hp, res, tot = len(speed), [], float('-inf'), 0
        lst = [[-efficiency[i], speed[i]] for i in range(n)]
        lst.sort()

        for eff, spd in lst:
            heapq.heappush(hp, spd)
            tot += spd
            if len(hp) > k:
                tot -= heapq.heappop(hp)
            res = max(res, tot * -eff)

        return res % (10**9 + 7)
