class Solution:
    def stoneGameVII(self, stones: list[int]) -> int:
        # Initialize memoization table
        memo = [[None] * len(stones) for _ in range(len(stones))]
        total_sum = sum(stones)
        
        def dfs(i, j, sum_, alice_turn):
            # Base case: no stones left
            if i == j:
                return 0
            
            # Check if already computed
            if memo[i][j] is not None:
                return memo[i][j]
            
            if alice_turn:  # Alice's turn, trying to maximize the gain
                left_choice = sum_ - stones[i] + dfs(i + 1, j, sum_ - stones[i], False)
                right_choice = sum_ - stones[j] + dfs(i, j - 1, sum_ - stones[j], False)
                memo[i][j] = max(left_choice, right_choice)
            else:  # Bob's turn, trying to minimize Alice's gain
                left_choice = dfs(i + 1, j, sum_ - stones[i], True) - (sum_ - stones[i])
                right_choice = dfs(i, j - 1, sum_ - stones[j], True) - (sum_ - stones[j])
                memo[i][j] = min(left_choice, right_choice)
            
            return memo[i][j]
        
        # Start the game with Alice's turn
        return dfs(0, len(stones) - 1, total_sum, True)

        
