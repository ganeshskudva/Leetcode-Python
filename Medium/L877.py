class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = defaultdict(int)

        def solve(start, end, turn=1):
            if end < start:
                return 0
            key = (start, end, turn)
            if key in dp:
                return dp[key]

            next_turn = abs(turn - 1)
            if turn:
                dp[key] = max(piles[start] + solve(start + 1, end, next_turn), piles[start] + solve(start, end - 1, next_turn))
            else:
                dp[key] = min(-piles[start] + solve(start + 1, end, next_turn), -piles[start] + solve(start, end - 1, next_turn))
            
            return dp[key]
    
        return solve(0, len(piles) - 1) >= 0
