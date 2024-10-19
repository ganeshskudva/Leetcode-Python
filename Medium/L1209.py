class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Initialize a stack to keep track of characters and their consecutive counts
        st = []

        # Iterate over each character in the string along with its index
        for i, ch in enumerate(s):
            # If the stack is not empty and the top character of the stack matches the current character
            if st and st[-1][0] == ch:
                # Increment the count of the character at the top of the stack
                st[-1][1] += 1
            else:
                # If the current character is not the same as the one on the stack, push it onto the stack with a count of 1
                st.append([ch, 1])

            # If the count of the top character in the stack equals `k`, remove it (because it's a duplicate)
            if st[-1][1] == k:
                st.pop()

        # Reconstruct the string by repeating each character in the stack based on its count
        return ''.join([ch * tot for ch, tot in st])

# Time Complexity (TC):
# The time complexity is O(n), where `n` is the length of the input string `s`. 
# Each character in the string is pushed and popped from the stack at most once. 
# Therefore, the overall time complexity is linear with respect to the size of the input string.

# Space Complexity (SC):
# The space complexity is O(n), where `n` is the length of the input string `s`.
# In the worst case, the stack will store all the characters of the input string with their counts (if no duplicates are removed).
# Hence, the space complexity is proportional to the size of the input string.
