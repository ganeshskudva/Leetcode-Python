class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # Initialize a defaultdict to keep track of each person's net balance
        # mp[s] -= a means person 's' loses 'a' amount
        # mp[d] += a means person 'd' gains 'a' amount
        mp = defaultdict(int)

        # Process each transaction: update balances of sender (s) and receiver (d)
        for s, d, a in transactions:
            mp[s] -= a
            mp[d] += a

        # Create a list of net balances (debt) from the dictionary values
        debt = list(mp.values())

        # Recursive function to minimize the number of transactions
        def solve(idx=0):
            res = float('inf')  # Initialize result to infinity, since we are minimizing transactions
            
            # Skip over any indices where the balance is already zero (no debt for that person)
            while idx < len(debt) and debt[idx] == 0:
                idx += 1

            # If we have processed all people, return 0 because no further transactions are needed
            if idx == len(debt):
                return 0

            # Try to find the minimum number of transactions by settling the current debt with other people
            for i in range(idx + 1, len(debt)):
                # Only attempt to settle if the debts have opposite signs (one owes, the other is owed)
                if debt[idx] * debt[i] < 0:
                    # Attempt to settle the debt by transferring the amount between idx and i
                    debt[i] += debt[idx]  # Settle the debt at index idx with person i
                    # Recursively solve for the remaining debts and count this transaction
                    res = min(res, 1 + solve(idx + 1))
                    # Backtrack: undo the transaction to explore other possibilities
                    debt[i] -= debt[idx]

            return res

        # Call the recursive function starting from index 0 and return the result
        return solve()
