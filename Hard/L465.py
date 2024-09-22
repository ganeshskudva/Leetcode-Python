from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        mp = defaultdict(int)
        
        # Step 1: Calculate net balances for all people based on transactions.
        # If someone is a sender (s), subtract the amount from their balance.
        # If someone is a receiver (d), add the amount to their balance.
        for s, d, a in transactions:
            mp[s] -= a  # Sender sends money, reducing their balance
            mp[d] += a  # Receiver receives money, increasing their balance
        
        # Step 2: Create a list of non-zero balances (debts).
        # Only include people who owe money or are owed money.
        debt = [bal for bal in mp.values() if bal != 0]

        # Recursive helper function to minimize the number of transactions required
        def solve(idx=0):
            # If all debts have been settled (i.e., all debts processed), return 0 transactions
            if idx == len(debt):
                return 0
            
            # Skip settled debts (balance of 0), continue to the next debt
            if debt[idx] == 0:
                return solve(idx + 1)
            
            res = float('inf')  # Set result to a large number to find the minimum transactions
            
            # Try to settle debt[idx] with any other person who has an opposite balance
            for i in range(idx + 1, len(debt)):
                # Only settle with people who have the opposite sign in their balance
                if debt[idx] * debt[i] < 0:  # One owes money, the other is owed money
                    # Settle debt[idx] with debt[i]
                    debt[i] += debt[idx]  # Add debt[idx] to debt[i], settling part of the debt
                    
                    # Recursively solve the remaining debts and count this settlement as 1 transaction
                    res = min(res, 1 + solve(idx + 1))
                    
                    # Backtrack: undo the settlement to explore other possibilities
                    debt[i] -= debt[idx]
            
            return res  # Return the minimum number of transactions found

        return solve()  # Start solving from the first debt (index 0)