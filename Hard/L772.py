class Solution:
    def calculate(self, s: str) -> int:
        def update(op, v):
            """
            Helper function to update the stack based on the current operator and value.
            Handles addition, subtraction, multiplication, and division.
            """
            if op == "+": 
                stack.append(v)  # Push positive value for addition
            if op == "-": 
                stack.append(-v)  # Push negative value for subtraction
            if op == "*": 
                stack.append(stack.pop() * v)  # Perform multiplication with the last value
            if op == "/": 
                stack.append(int(stack.pop() / v))  # Perform integer division with truncation toward zero

        it, num, stack, sign = 0, 0, [], "+"  # Initialize variables

        while it < len(s):
            if s[it].isdigit():
                # Build the current number if digits are found
                num = num * 10 + int(s[it])
            elif s[it] in "+-*/":
                # When an operator is encountered, update the stack with the previous number
                update(sign, num)
                num, sign = 0, s[it]  # Reset the number and update the operator
            elif s[it] == "(":  # Handle parentheses recursively for BC I and BC III
                # Calculate the result for the expression inside parentheses
                num, j = self.calculate(s[it + 1:])
                it += j  # Move the iterator forward by the length of the processed substring
            elif s[it] == ")":  # End of a subexpression
                # Update the stack with the last number and return the result for this subexpression
                update(sign, num)
                return sum(stack), it + 1  # Return the total sum and the length processed
            it += 1  # Move to the next character

        # Update for the last number in the expression
        update(sign, num)
        return sum(stack)  # Return the total result of the expression

# Time Complexity (TC): O(n)
# Explanation:
# - Each character in the string is processed exactly once.
# - Recursive calls divide the input into smaller substrings, but the total work across all calls is O(n).
# - No nested loops or expensive operations, making this a linear solution.

# Space Complexity (SC): O(n)
# Explanation:
# - The stack stores numbers and intermediate results, which can grow up to O(n) in the worst case (e.g., a long expression with many operators).
# - Recursive calls add to the call stack, which also contributes O(n) space in the worst case of deeply nested parentheses.
# - Total space complexity: O(n).
