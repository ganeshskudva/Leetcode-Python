class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Helper function to recursively solve the problem
        def solve(idx=0, st=None):
            if not st:
                st = set()  # Initialize a set to keep track of unique substrings
            
            # Base case: If we've reached the end of the string
            if idx >= len(s):
                return 0  # No more substrings to split, so return 0
            
            res = -1  # Initialize result to -1 to track the maximum number of unique splits
            
            # Explore all possible splits from the current index
            for i in range(idx + 1, len(s) + 1):
                sub = s[idx : i]  # Take the substring from idx to i
                if sub in st:  # If this substring is already used, skip it
                    continue
                
                st.add(sub)  # Add the current substring to the set of unique substrings
                nxt = solve(i, st)  # Recursively solve the problem for the remaining part of the string
                
                if nxt >= 0:
                    # If valid, update the result to maximize the number of unique splits
                    res = max(res, nxt + 1)
                
                st.remove(sub)  # Backtrack by removing the substring from the set
            
            return res
        
        return solve()  # Start solving from the beginning of the string

# Time Complexity (TC): O(n * 2^n), where n is the length of the string.
#   - There are at most 2^n possible ways to split the string into unique parts, since each character can either start a new substring or continue the current one.
#   - For each split, the algorithm checks whether the substring is unique by performing set operations, which are O(1) on average.
#   - The overall time complexity is dominated by the exponential number of possible splits.

# Space Complexity (SC): O(n), where n is the length of the string.
#   - The recursion depth can go up to O(n) due to the recursive call stack.
#   - The set `st` that stores the unique substrings can also hold up to O(n) elements at most, as each character in the string could form its own unique substring in the worst case.
