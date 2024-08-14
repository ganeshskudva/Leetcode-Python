class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp, n = defaultdict(int), len(days)
        
        @cache
        def solve(idx):
            if idx >= n:
                return 0
            if idx in dp:
                return dp[idx]
            
            cost_day = costs[0] + solve(idx + 1)
           
            i = idx
            while i < n and days[i] < days[idx] + 7:
                i += 1
            cost_week = costs[1] + solve(i)
            
            i = idx 
            while i < n and days[i] < days[idx] + 30:
                i += 1
            cost_month = costs[2] + solve(i)
            
            return min(cost_day, cost_week, cost_month)
        
        return solve(0)
