class Solution:
    # The maxProfit function takes in a list of prices and returns the maximum possible profit
    # by performing at most one transaction (buy and then sell).
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize a dictionary to store subproblem solutions, which helps to avoid recomputation.
        dp = defaultdict(int)

        # Define a recursive helper function `solve` to compute the maximum profit.
        # Parameters:
        # - i: the current index in the prices list (represents the day we are considering).
        # - k: the number of remaining transactions (we only have one transaction in this case).
        # - buy: a boolean indicating whether we are allowed to buy stock on the current day.
        def solve(i, k, buy=True):
            # Base case 1: If we have processed all the days or no transactions are left, return 0.
            # There is no profit to be made after the last day or without any transactions left.
            if i >= len(prices) or k <= 0:
                return 0

            # Memoization: If we have already solved this subproblem (for day `i` and buy state),
            # return the stored result to avoid redundant computations.
            if (i, buy) in dp:
                return dp[(i, buy)]

            # If we are allowed to buy on the current day
            if buy:
                # We have two choices:
                # 1. Buy the stock on day `i` and then solve for the next day (i+1) with buy set to False.
                #    This reduces our cash by prices[i] (the cost of buying the stock).
                # 2. Skip buying and move to the next day without changing our state.
                dp[(i, buy)] = max(-prices[i] + solve(i + 1, k, not buy),  # Buy stock
                                   solve(i + 1, k, buy))                 # Skip buying

            # If we are allowed to sell on the current day
            else:
                # We have two choices:
                # 1. Sell the stock on day `i` and then solve for the next day (i+1), reducing the number
                #    of transactions left (k-1). This increases our cash by prices[i] (the selling price).
                # 2. Skip selling and move to the next day without changing our state.
                dp[(i, buy)] = max(prices[i] + solve(i + 1, k - 1, not buy),  # Sell stock
                                   solve(i + 1, k, buy))                    # Skip selling

            # Return the result stored in dp for this subproblem.
            return dp[(i, buy)]

        # Call the recursive function starting from day 0, with 1 transaction left and initially allowed to buy.
        return solve(0, 1)

        
