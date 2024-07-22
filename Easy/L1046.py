class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        for s in stones:
            heapq.heappush(hp, -s)

        while len(hp) > 1:
            x, y = -heapq.heappop(hp), -heapq.heappop(hp)
            if x != y:
                heapq.heappush(hp, -abs(x - y))

        return -hp[0] if hp else 0
