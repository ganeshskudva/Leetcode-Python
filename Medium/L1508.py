class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        hp = [(nums[i], i + 1) for i in range(n)]
        heapq.heapify(hp)
        res, mod = 0, 1000000007

        for i in range(1, right + 1):
            tot, idx = heapq.heappop(hp)
            if i >= left:
                res = (res + tot) % mod
            if idx < n:
                heapq.heappush(hp, (tot + nums[idx], idx + 1))

        return res
