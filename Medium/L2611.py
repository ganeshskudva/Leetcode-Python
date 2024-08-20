class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        res, hp = sum(reward2), [-(reward1[i] - reward2[i]) for i in range(len(reward1))]
        heapq.heapify(hp)

        while k:
            res += -1 * heapq.heappop(hp)
            k -= 1

        return res
