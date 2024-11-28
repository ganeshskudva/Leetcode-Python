class Solution:
    def calculate(self, s: str):
        # Helper function to update the stack based on the current operator and value
        def update(op, v):
            if op == "+": 
                stack.append(v)  # Push the value for addition
            if op == "-": 
                stack.append(-v)  # Push the negative value for subtraction
            if op == "*": 
                stack.append(stack.pop() * v)  # Multiply top of the stack for BC II and BC III
            if op == "/": 
                stack.append(int(stack.pop() / v))  # Integer division for BC II and BC III
        
        it, num, stack, sign = 0, 0, [], "+"  # Initialize iterator, number, stack, and initial sign
        
        # Iterate through the string
        while it < len(s):
            if s[it].isdigit():
                # Build the current number
                num = num * 10 + int(s[it])
            elif s[it] in "+-*/":
                # When an operator is encountered, update the stack with the previous number
                update(sign, num)
                num, sign = 0, s[it]  # Reset the number and update the sign/operator
            elif s[it] == "(":
                # For BC I and BC III: handle subexpression recursively
                num, j = self.calculate(s[it + 1:])  # Calculate inside parentheses
                it = it + j  # Skip the processed substring
            elif s[it] == ")":
                # For BC I and BC III: end of subexpression, return the result
                update(sign, num)
                return sum(stack), it + 1  # Return the sum and the length processed
            it += 1
        # Update for the last number in the string
        update(sign, num)
        return sum(stack)  # Return the total sum of the stack

# Time Complexity (TC): O(n)
# Explanation:
# - Each character in the string is processed exactly once, making this O(n).
# - Recursive calls for parentheses handle smaller substrings, but still, each character is visited once in total.

# Space Complexity (SC): O(n)
# Explanation:
# - The stack stores numbers for each operation, which can grow to O(n) in the worst case (e.g., all numbers with no operators).
# - Recursive calls for subexpressions add to the call stack, contributing additional O(n) space in the worst case of deeply nested parentheses.
# - Total space complexity: O(n).
