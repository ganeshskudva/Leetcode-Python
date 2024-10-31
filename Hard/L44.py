class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        memo = {}  # Memoization dictionary to store already computed results

        def solve(i=0, j=0):
            # Check if the result of this subproblem is already computed
            if (i, j) in memo:
                return memo[(i, j)]

            # If both i and j have reached the end of their respective strings, match is found
            if i >= len(s) and j >= len(p):
                memo[(i, j)] = True
            # If only j has reached the end of pattern, there is no match
            elif j >= len(p):
                memo[(i, j)] = False
            # If only i has reached the end of s
            elif i >= len(s):
                # Remaining pattern must be only '*' characters to match an empty string
                memo[(i, j)] = all(x == '*' for x in p[j:])
            # Optimized handling of '*'
            elif p[j] == '*':
                # Match '*' to zero characters in `s` (solve(i, j + 1)) or
                # match '*' to one character in `s` (solve(i + 1, j))
                memo[(i, j)] = solve(i, j + 1) or solve(i + 1, j)
            # If current character in pattern is '?' or matches current character in s
            elif p[j] == '?' or p[j] == s[i]:
                memo[(i, j)] = solve(i + 1, j + 1)
            else:
                # Characters do not match
                memo[(i, j)] = False

            return memo[(i, j)]

        return solve()

# Time Complexity (TC): O(m * n)
# - The time complexity is still O(m * n) because each (i, j) state is computed at most once and stored in memo.
# - This is optimal since every character in `s` and `p` must be considered for matching.

# Space Complexity (SC): O(m * n)
# - Memoization table stores up to O(m * n) entries.
# - The recursion stack can reach a depth of O(m + n) in the worst case, but memoization prevents redundant calls.
