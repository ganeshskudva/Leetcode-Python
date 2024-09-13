class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []  # List to store all valid expressions that evaluate to the target
        
        # Edge case: If the input string is empty, return an empty result list
        if not num:
            return res

        # Helper function to recursively build expressions
        def solve(path="", pos=0, tot=0, mult=0):
            # Base case: If we've processed all characters in 'num'
            if pos == len(num):
                # If the current total matches the target, add the expression to the result
                if target == tot:
                    res.append(path)
                return

            # Try to form numbers by choosing substrings of 'num'
            for i in range(pos, len(num)):
                # If the current substring starts with '0' and isn't just '0', skip (no leading zero numbers)
                if i != pos and num[pos] == '0':
                    break

                # Extract current substring and convert it to an integer
                curr = num[pos: i + 1]
                int_crr = int(curr)

                # If this is the first number (no operators yet), initialize the expression with it
                if not pos:
                    solve(path + curr, i + 1, int_crr, int_crr)
                else:
                    # Addition case: Add '+' before the current number
                    solve(path + "+" + curr, i + 1, tot + int_crr, int_crr)

                    # Subtraction case: Add '-' before the current number
                    solve(path + "-" + curr, i + 1, tot - int_crr, -int_crr)

                    # Multiplication case: Add '*' before the current number
                    # Special care is needed to ensure multiplication precedence is handled properly
                    solve(path + "*" + curr, i + 1, tot - mult + mult * int_crr, mult * int_crr)

        # Start the recursive process with an empty path, starting position 0, and initial total 0
        solve()
        
        # Return the list of valid expressions
        return res
