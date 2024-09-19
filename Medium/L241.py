class Solution:
    def diffWaysToCompute(self, expr: str) -> List[int]:
        # Memoization map to store results of sub-expressions and avoid recomputation
        memo = {}

        # Define the recursive function using closure to access the memoization map
        def compute(expression: str) -> List[int]:
            # Check if the result for the current expression is already memoized
            if expression in memo:
                return memo[expression]

            # Initialize an empty list to store possible results for the current expression
            res = []
            # Set of valid operators we will evaluate
            op = {'+', '-', '*'}

            # Loop through each character in the expression
            for i, ch in enumerate(expression):
                # If the current character is an operator, we can divide the expression
                if ch in op:
                    # Split the expression into two parts: left and right of the operator
                    left_part = expression[:i]
                    right_part = expression[i + 1:]

                    # Recursively compute all possible results for both left and right parts
                    left_results = compute(left_part)
                    right_results = compute(right_part)

                    # Combine the results from both left and right sub-expressions
                    for l in left_results:
                        for r in right_results:
                            # Apply the current operator between results from left and right
                            if ch == '+':
                                res.append(l + r)  # Addition
                            elif ch == '-':
                                res.append(l - r)  # Subtraction
                            else:  # ch == '*'
                                res.append(l * r)  # Multiplication

            # Base case: if no operator was found, the expression is a number
            if not res:
                res.append(int(expression))  # Convert the entire expression to an integer

            # Store the computed result for the current expression in the memo map
            memo[expression] = res

            # Return the list of all possible results for the current expression
            return res

        # Initiate the recursive closure starting with the full expression
        return compute(expr)
