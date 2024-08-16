class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        dp = defaultdict(int)
        
        def solve(idx, prev_val=float('-inf')):
            if idx >= len(pairs):
                return 0
            key = (idx, prev_val)
            if key in dp:
                return dp[key]
            
            include, skip = 0, 0
            if pairs[idx][0] > prev_val:
                include = 1 + solve(idx + 1, pairs[idx][1])
            skip = solve(idx + 1, prev_val)
            
            dp[key] = max(include, skip)
            return dp[key]
        
        return solve(0)
