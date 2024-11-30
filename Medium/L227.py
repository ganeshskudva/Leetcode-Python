class Solution:
    def calculate(self, s):    
        """
        Evaluates a mathematical expression given as a string containing
        integers, operators (+, -, *, /), and parentheses.

        Parameters:
        s (str): The input mathematical expression.

        Returns:
        int: The result of the evaluated expression.
        """
        def calc(it):
            """
            Recursive function to evaluate the expression starting from index `it`.

            Parameters:
            it (int): Current index in the string `s`.

            Returns:
            tuple: The result of the evaluation and the next index to process.
            """
            def update(op, v):
                """
                Updates the stack based on the current operator and value.

                Parameters:
                op (str): The current operator (+, -, *, /).
                v (int): The current value to apply the operator on.
                """
                if op == "+":
                    stack.append(v)
                elif op == "-":
                    stack.append(-v)
                elif op == "*":
                    stack.append(stack.pop() * v)
                elif op == "/":
                    stack.append(int(stack.pop() / v))  # Integer division truncates towards zero
        
            num, stack, sign = 0, [], "+"  # Initialize the current number, stack, and default sign
            
            while it < len(s):
                if s[it].isdigit():
                    # Accumulate the digit into the current number
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    # Update the stack with the current number and operator, reset for the next number
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    # Handle nested expressions by recursion
                    num, j = calc(it + 1)
                    it = j - 1  # Update the index to skip the processed sub-expression
                elif s[it] == ")":
                    # Close the current parentheses by updating the stack and returning the result
                    update(sign, num)
                    return sum(stack), it + 1
                it += 1
            
            # Final update for the last number in the expression
            update(sign, num)
            return sum(stack)

        return calc(0)

# Detailed Time Complexity:
# - Each character in the input string `s` is processed exactly once in the main loop or during recursion.
# - Operators (+, -, *, /) and parentheses trigger constant-time operations like stack updates or recursion.
# - Therefore, the overall time complexity is O(n), where `n` is the length of the string.

# Detailed Space Complexity:
# - The stack is used to store intermediate results for nested parentheses.
# - In the worst case (highly nested expressions), the stack can grow to O(n).
# - Therefore, the space complexity is O(n) for the stack usage.
