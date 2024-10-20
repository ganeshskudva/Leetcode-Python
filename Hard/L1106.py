class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # Initialize a stack to keep track of parsed elements
        stack = []
        
        # Iterate through each character in the expression
        for c in expression:
            if c == ')':  # When a closing parenthesis is found, process the subexpression inside it
                true_count = false_count = 0  # Counters to track the number of True and False values
                
                # Pop elements from the stack until we encounter an opening parenthesis '('
                while stack[-1] != '(':
                    val = stack.pop()  # Pop the top value
                    if val:
                        true_count += 1  # Increment the true_count if value is True
                    else:
                        false_count += 1  # Increment the false_count if value is False
                
                stack.pop()  # Pop the opening parenthesis '('
                operator = stack.pop()  # Pop the operator ('&', '|', or '!')
                
                # Apply the logic based on the operator
                if operator == '&':
                    # '&' (AND) requires all values to be True, so we check if false_count is zero
                    stack.append(false_count == 0)  # Push True if no False values were encountered
                elif operator == '|':
                    # '|' (OR) requires at least one value to be True, so we check if true_count > 0
                    stack.append(true_count > 0)  # Push True if at least one True value was encountered
                else:  # '!' operator (NOT)
                    # '!' only negates a single value, so if we have any True value, push False, and vice versa
                    stack.append(not (true_count > 0))  # Push the negated result of the single boolean value
            elif c != ',':  # Ignore commas as they are just delimiters
                # Convert 't' and 'f' to True and False respectively and push them onto the stack
                # Operators ('&', '|', '!') and parentheses are also pushed directly to the stack
                stack.append(True if c == 't' else False if c == 'f' else c)
        
        # At the end of parsing, the stack will contain only one element which is the result of the boolean expression
        return stack.pop()

# Time Complexity (TC): O(n), where n is the length of the expression.
# We iterate through each character in the expression exactly once. The stack operations (push, pop) are constant-time operations (O(1)).

# Space Complexity (SC): O(n), where n is the length of the expression.
# The stack can grow to hold most of the elements of the expression, so the space usage is proportional to the size of the input.
