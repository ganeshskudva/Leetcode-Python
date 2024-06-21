class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        mp, m, n = defaultdict(int), len(arr2), len(arr1)
        
        for i in range(n):
            x = arr1[i]
            while x > 0:
                mp[x] = len(str(x))
                x //= 10
        res = 0
        for i in range(m):
            y = arr2[i]
            while y > 0:
                if y in mp:
                    res = max(res, mp[y])
                y //= 10
        
        return res
