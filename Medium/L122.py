class Solution:
    # The maxProfit function takes in a list of prices and returns the maximum possible profit
    # by performing unlimited transactions (buy and then sell).
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize a dictionary (dp) to store the results of subproblems. 
        # The key will be a tuple of (idx, buy), where:
        # - idx: the current day (index in the prices list).
        # - buy: a boolean indicating if we are allowed to buy on that day.
        # The value will be the maximum profit obtainable from that day with that state.
        dp = defaultdict(int)

        # Define a recursive helper function `solve` that calculates the maximum profit.
        # Parameters:
        # - idx: the current index in the prices list (representing the day).
        # - buy: a boolean flag indicating whether we are in a "buying" state.
        def solve(idx, buy=True):
            # Base case: If we've processed all the days, no more transactions are possible,
            # so the profit is 0.
            if idx >= len(prices):
                return 0

            # Memoization: If the subproblem for the current day and "buy" state has already been solved,
            # return the cached result to avoid recomputation.
            if (idx, buy) in dp:
                return dp[(idx, buy)]

            # If we are allowed to buy on the current day
            if buy:
                # We have two choices:
                # 1. Buy the stock on the current day (subtract prices[idx] from our profit),
                #    then move to the next day in the "sell" state (buy=False).
                # 2. Skip buying and move to the next day, staying in the "buy" state.
                dp[(idx, buy)] = max(-prices[idx] + solve(idx + 1, not buy),  # Buy stock
                                     solve(idx + 1, buy))                   # Skip buying

            # If we are in the "sell" state (i.e., holding a stock we can sell)
            else:
                # We have two choices:
                # 1. Sell the stock on the current day (add prices[idx] to our profit),
                #    then move to the next day in the "buy" state (buy=True).
                # 2. Skip selling and move to the next day, staying in the "sell" state.
                dp[(idx, buy)] = max(prices[idx] + solve(idx + 1, not buy),   # Sell stock
                                     solve(idx + 1, buy))                    # Skip selling

            # Store the result of this subproblem in the dp dictionary.
            return dp[(idx, buy)]

        # The recursion starts from day 0 (idx=0) and initially we are allowed to buy (buy=True).
        return solve(0)
