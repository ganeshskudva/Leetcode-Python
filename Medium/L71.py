class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []  # Stack to store the valid components of the path

        # Split the path by "/" and process each component
        for s in path.split("/"):
            if s == '..':
                if st:  # Pop from stack if possible
                    st.pop()
            elif s != "" and s != '.':  # Ignore empty strings and '.'
                st.append(s)

        # Join the stack components with '/' to form the simplified path
        return '/' + '/'.join(st)

# Time Complexity (TC): O(n), where n is the length of the input string.
# - Splitting the string by '/' takes O(n).
# - Iterating through the components and performing operations on the stack takes O(n).
# Total: O(n).

# Space Complexity (SC): O(n)
# - The stack `st` can store up to O(n) components in the worst case.
# - The result string also takes O(n) space.
# Total: O(n).


