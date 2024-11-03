class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize the result list to store all valid combinations of parentheses
        res = []
        if not n:
            return res

        # Helper function to recursively generate combinations
        # open_idx: count of '(' used so far
        # close_idx: count of ')' used so far
        # tmp: temporary list to build the current combination
        def solve(open_idx, close_idx, tmp=None):
            if tmp is None:
                tmp = []

            # Base case: if tmp has length 2 * n, we've formed a valid combination
            if len(tmp) == 2 * n:
                res.append(''.join(tmp))  # Join list to string and add to result
                return

            # If we can still add more '(', do so
            if open_idx < n:
                tmp.append('(')  # Add '(' to the current combination
                solve(open_idx + 1, close_idx, tmp)  # Recur with incremented open count
                del tmp[-1]  # Backtrack to try other possibilities

            # If we can add more ')' (without exceeding open '('), do so
            if close_idx < open_idx:
                tmp.append(')')  # Add ')' to the current combination
                solve(open_idx, close_idx + 1, tmp)  # Recur with incremented close count
                del tmp[-1]  # Backtrack to try other possibilities

        # Initial call to solve function
        solve(0, 0)
        return res

# Overall Time Complexity (TC): O(4^n / sqrt(n)), which is the Catalan number
# for generating well-formed parentheses combinations. This is the number of unique combinations.

# Overall Space Complexity (SC): O(n), where n is the depth of the recursive call stack.
# Additionally, each combination of parentheses is stored in the result list `res`, which takes O(4^n / sqrt(n)) space.
