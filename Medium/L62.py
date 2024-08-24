class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mp = defaultdict(int)
        
        def isValid(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def solve(x=0, y=0):
            if not isValid(x, y):
                return 0
            if x == m - 1 and y == n - 1:
                return 1
            
            key = (x, y)
            if key in mp:
                return mp[key]
            
            mp[key] = solve(x + 1, y) + solve(x, y + 1)
            return mp[key]
        
        return solve()
