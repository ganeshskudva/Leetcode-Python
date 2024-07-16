class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return -1 * (x**2 + y**2)

        hp, res = [], []
        for px, py in points:
            hp.append((dist(px, py), px, py))

        heapq.heapify(hp)
        while len(hp) > k:
            heapq.heappop(hp)

        return [(x, y) for _, x, y in hp]
