class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mp = defaultdict(int)
        
        def solve(n):
            if n < 0:
                return 0
            if n == 0 or n == 1:
                return cost[n]
            if n in mp:
                return mp[n]
            mp[n] = cost[n] + min(solve(n - 1), solve(n - 2))
            return mp[n]
        
        return min(solve(len(cost) - 1), solve(len(cost) - 2))
