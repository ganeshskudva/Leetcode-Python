class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_til_now, res = heights[-1], [len(heights) - 1]

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > max_til_now:
                res.append(i)
            max_til_now = max(max_til_now, heights[i])

        return res[::-1]
