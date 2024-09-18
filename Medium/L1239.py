class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Initialize a result list where res[0] stores the maximum length found
        res = [0]

        # Helper function to check if a string has all unique characters
        def is_unique(s):
            # Convert string to a set and compare its length with the original string
            # If lengths are the same, it means all characters are unique
            return len(set(s)) == len(s)

        # Backtracking function to explore all possible concatenations of strings
        def solve(path='', idx=0):
            # Check if the current concatenation `path` is unique
            unique = is_unique(path)

            # If the current concatenation is unique and longer than the previously found max length
            if unique and len(path) > res[0]:
                # Update the result with the new maximum length
                res[0] = len(path)

            # If we reach the end of the array or the current path is not unique, we stop further exploration
            if idx == len(arr) or not unique:
                return

            # Iterate over the array starting from the current index `idx`
            for i in range(idx, len(arr)):
                # Recursively call `solve` by concatenating the current string `arr[i]` to `path`
                # Move to the next index `i + 1` to avoid reusing the same string
                solve(path + arr[i], i + 1)

        # Start the backtracking with an empty path and at the 0th index of the array
        solve()

        # Return the maximum length found
        return res[0]