class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize result and stack for directory names
        res, st = [], []
        
        # Split the path by "/" and process each component
        for s in path.split("/"):
            # ".." means to go up one directory, so pop from stack if possible
            if s == '..':
                if st:
                    st.pop()
            # Ignore empty components and "." (current directory)
            elif s != "" and s != '.':
                st.append(s)  # Add directory to stack if it's a valid name
        
        # If the stack is empty, return the root "/"
        if not st:
            return "/"
        
        # Build the simplified path by appending '/' and each directory in the stack
        for c in st:
            res.append('/')
            res.append(c)
                
        return ''.join(res)  # Join the result list into a string

# Time Complexity (TC):
# - Splitting the path by "/" is O(n), where n is the length of the input string `path`.
# - We iterate over each component in the split path and perform constant-time operations (append/pop) on the stack.
# - The final loop that builds the result path is also O(n), as it iterates through the stack.
# - Overall, the time complexity is O(n).

# Space Complexity (SC):
# - The stack `st` stores the directory names, with at most one element per directory in the path, making it O(n).
# - The result list `res` is also O(n) in the worst case for building the final simplified path.
# - Overall space complexity is O(n).

