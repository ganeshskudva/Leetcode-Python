class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = float('-inf')
        mx, mn = arrays[0][-1], arrays[0][0]

        for i in range(1, len(arrays)):
            curr_min, curr_max = arrays[i][0], arrays[i][-1]
            
            res = max(res, abs(curr_min - mx))
            res = max(res, abs(curr_max - mn))
            
            mx, mn = max(mx, curr_max), min(mn, curr_min)
        
        return res
