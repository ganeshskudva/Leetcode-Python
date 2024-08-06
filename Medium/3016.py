class Solution:
    def minimumPushes(self, word: str) -> int:
        hp = [-v for _, v in collections.Counter(word).items()]
        heapq.heapify(hp)
        tot, key_pos = 0, 0

        while hp:
            tot += (key_pos // 8 + 1) * -heapq.heappop(hp)
            key_pos += 1

        return tot
