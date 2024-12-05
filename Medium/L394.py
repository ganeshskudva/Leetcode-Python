class Solution(object):
    def decodeString(self, s):
        # Stack to keep track of previous strings and repetition numbers
        stack_ = []
        # Variables to store the current number and current string being constructed
        cur_num = 0
        cur_str = []

        for c in s:
            if c == '[':
                # Push the current string and number onto the stack
                stack_.append(cur_str)
                stack_.append(cur_num)
                # Reset current string and number for the new context
                cur_str = []
                cur_num = 0
            elif c == ']':
                # Pop the number and previous string from the stack
                num = stack_.pop()
                prevString = stack_.pop()
                # Update the current string by repeating it and appending it to the previous string
                cur_str = prevString + num * cur_str
            elif c.isdigit():
                # Handle multiple-digit numbers
                cur_num = cur_num * 10 + int(c)
            else:
                # Add characters to the current string
                cur_str.append(c)

        # Return the final decoded string
        return ''.join(cur_str)

# Time Complexity (TC): O(n)
# - We iterate through the input string `s` once, processing each character in O(1).
# - Constructing the `curString` involves appending or repeating, which is efficient due to stack usage.
# - The overall complexity is O(n), where n is the length of the input string.

# Space Complexity (SC): O(m)
# - The stack can store up to O(m) characters and numbers, where m is the depth of nested brackets.
# - The final decoded string is returned, requiring O(k) space, where k is the length of the output.
# - Total space complexity is O(m + k).
