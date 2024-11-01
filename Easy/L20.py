class Solution:
    def isValid(self, s: str) -> bool:
        # If the length of the string is odd, it can't be valid.
        if len(s) % 2 != 0:
            return False

        # Mapping of opening brackets to their corresponding closing brackets.
        mp = {'(': ')', '{': '}', '[': ']'}
        
        # Stack to keep track of the expected closing brackets.
        st = []

        # Iterate over each character in the input string.
        for c in s:
            if c in mp:  
                # If the character is an opening bracket, push the corresponding closing bracket.
                st.append(mp[c])
            elif not st or st[-1] != c:
                # If stack is empty or current closing bracket doesn't match the top of the stack.
                return False
            else:
                # Otherwise, pop the stack as the current closing bracket matches.
                st.pop()

        # In the end, the stack should be empty if all brackets were matched correctly.
        return not st

# Time Complexity (TC): O(n), where n is the length of the input string `s`.
#   - We iterate over each character in `s` once, performing constant-time operations per character.

# Space Complexity (SC): O(n), where n is the length of the input string `s`.
#   - In the worst case, if all characters are opening brackets, the stack `st` will hold up to `n` elements.
#   - This could be optimized to O(k), where k is the maximum depth of nested brackets,
#     but for general purposes, we consider the space to be O(n).


