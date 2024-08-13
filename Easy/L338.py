class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        
        def solve(n):
            if not n:
                return n
            
            key = n & (n - 1)
            if res[key] != 0:
                return res[key] + 1
            
            res[n] = solve(key) + 1
            return res[n]
        
        for i in range(1, num + 1):
            res[i] = solve(i & (i - 1)) + 1
        
        return res
