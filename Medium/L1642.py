class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hp = []
        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                heapq.heappush(hp, d)
            if len(hp) > ladders:
                bricks -= heapq.heappop(hp)
            if bricks < 0:
                return i
        
        return len(heights) - 1
