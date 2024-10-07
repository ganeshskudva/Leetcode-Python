class Solution:
    def minLength(self, s: str) -> int:
        # Initialize an empty stack to process the string
        # TC: O(n), where n is the length of the string `s`
        # SC: O(n), in the worst case, all characters are added to the stack
        st = []

        # Traverse through each character in the string `s`
        for ch in s:
            # If the current character is 'B' and the stack's top element is 'A', remove the top element ('A')
            if ch == 'B':
                if st and st[-1] == 'A':  # Check if the top of the stack is 'A'
                    st.pop()  # Remove 'A' as it forms the pair 'AB'
                else:
                    st.append(ch)  # Otherwise, push 'B' onto the stack
            # If the current character is 'D' and the stack's top element is 'C', remove the top element ('C')
            elif ch == 'D':
                if st and st[-1] == 'C':  # Check if the top of the stack is 'C'
                    st.pop()  # Remove 'C' as it forms the pair 'CD'
                else:
                    st.append(ch)  # Otherwise, push 'D' onto the stack
            # For any other character, push it onto the stack
            else:
                st.append(ch)

        # The length of the stack is the result since it represents the remaining characters
        return len(st)
