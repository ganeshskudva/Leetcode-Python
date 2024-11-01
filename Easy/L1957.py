class Solution:
    def makeFancyString(self, s: str) -> str:
        # Initialize an empty stack to hold characters and their counts
        st = []

        # Traverse each character in the input string
        for ch in s:
            # Check if the stack is not empty
            if st:
                # If the last character in the stack is the same as the current character
                if st[-1][0] == ch:
                    # If the last character already has a count of 2, skip adding this character
                    if st[-1][1] == 2:
                        continue
                    else:
                        # Increment the count of the last character in the stack
                        st[-1][1] += 1
                else:
                    # If the current character is different from the last, add it with count 1
                    st.append([ch, 1])
            else:
                # If the stack is empty, initialize with the first character and count 1
                st.append([ch, 1])

        # Join the characters based on their counts and return the result
        return ''.join(ch * freq for ch, freq in st)

# Time Complexity (TC): O(n), where n is the length of the input string `s`.
#   - We iterate over each character in `s` once, performing constant-time operations per character.
#   - Building the final string is also O(n) as each character appears at most twice.

# Space Complexity (SC): O(n), where n is the length of the input string `s`.
#   - In the worst case, every character is unique or only appears once or twice in succession,
#     resulting in a list `st` with up to `n` elements.
