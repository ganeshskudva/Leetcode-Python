class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        mp = collections.Counter(heights)
        res, idx = 0, 1

        for h in heights:
            while not mp[idx]:
                idx += 1
            if h != idx:
                res += 1
            mp[idx] -= 1
        
        return res
