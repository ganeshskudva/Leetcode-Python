class Solution:
    def calculate(self, s: str) -> int:    
        def calc(it: int):
            # Helper function to update the stack based on the current operation and value
            def update(op, v):
                if op == "+":
                    stack.append(v)                    # Append the value for addition.
                if op == "-":
                    stack.append(-v)                   # Append the negative value for subtraction.
                if op == "*":
                    stack.append(stack.pop() * v)       # Perform multiplication on the last value and the current number.
                if op == "/":
                    stack.append(int(stack.pop() / v))  # Perform integer division on the last value and the current number.

            # Initialize variables: num for the current number, stack to hold values, sign for current operator.
            num, stack, sign = 0, [], "+"

            # Iterate through the string starting from index 'it'
            while it < len(s):
                if s[it].isdigit():                    # If the current character is a digit.
                    num = num * 10 + int(s[it])        # Build the current number (account for multi-digit numbers).
                elif s[it] in "+-*/":                  # If an operator is encountered.
                    update(sign, num)                  # Update the stack with the current number based on the previous sign.
                    num, sign = 0, s[it]               # Reset the number and update the sign to the current operator.
                elif s[it] == "(":                     # If an opening parenthesis is encountered.
                    num, tmp = calc(it + 1)            # Recursively call calc for the inner expression.
                    it = tmp - 1                       # Adjust 'it' to the position after the nested expression.
                elif s[it] == ")":                     # If a closing parenthesis is encountered.
                    update(sign, num)                  # Process the current number before closing the parentheses.
                    return sum(stack), it + 1          # Return the sum of the current stack and the position after the closing parenthesis.
                it += 1
            update(sign, num)                          # Process the last number after the loop finishes.
            return sum(stack)                          # Return the sum of the stack for the outermost expression.

        # Begin processing the expression starting at index 0.
        return calc(0)

# Time Complexity (TC):
# 1. The function iterates over the entire input string 's', which takes O(n) time, where 'n' is the length of 's'.
# 2. Each digit, operator, or parenthesis is processed exactly once during the traversal.
# 3. Recursive calls for expressions within parentheses are also processed in a linear manner, but since each character is processed once, the recursion does not increase the time complexity.
# Therefore, the overall time complexity is O(n), where 'n' is the length of the input string 's'.

# Space Complexity (SC):
# 1. The stack used to store intermediate results takes O(n) space in the worst case, where 'n' is the length of the input string.
# 2. The recursion depth can be as large as O(n) in the case of deeply nested parentheses.
# 3. Additional variables such as 'num', 'sign', and 'it' take constant space O(1).
# Therefore, the overall space complexity is O(n) due to the stack and recursion.
