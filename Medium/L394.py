class Solution(object):
    def decodeString(self, s):
        # Initialize a stack to keep track of previous strings and numbers
        stack = []
        # Variables to store the current number and current string being constructed
        curNum = 0
        curString = ''
        
        # Iterate through each character in the input string
        for c in s:
            # If the character is an opening bracket '[', push the current string and number onto the stack
            if c == '[':
                stack.append(curString)  # Save the current string before entering a new context
                stack.append(curNum)     # Save the current number for the next repeated sequence
                # Reset the current string and number for the new context inside the brackets
                curString = ''
                curNum = 0
            
            # If the character is a closing bracket ']', pop from the stack and build the new string
            elif c == ']':
                num = stack.pop()        # Retrieve the number of repetitions from the stack
                prevString = stack.pop() # Retrieve the previous string context from the stack
                # Update the current string by repeating the current string `num` times and appending it to the previous string
                curString = prevString + num * curString
            
            # If the character is a digit, build the current number (could be more than one digit)
            elif c.isdigit():
                # Update curNum to handle multiple-digit numbers (e.g., "34" becomes 34, not 3 and 4 separately)
                curNum = curNum * 10 + int(c)
            
            # If the character is a letter, add it to the current string being constructed
            else:
                curString += c
        
        # After finishing the iteration, return the final decoded string
        return curString
