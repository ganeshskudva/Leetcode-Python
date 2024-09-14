class Solution:
    def minInsertions(self, s: str) -> int:
        # Dictionary to store already computed results (memoization)
        dp = {}
        
        # Helper function 'solve' computes the minimum insertions required
        # to make the substring s[start:end+1] a palindrome.
        def solve(start=0, end=len(s)-1):
            # Base case: if 'start' passes 'end' or they are equal, the substring is already a palindrome,
            # so no insertions are needed.
            if start >= end:
                return 0

            # Create a tuple (start, end) as the key for memoization
            key = (start, end)

            # If the result for this range is already computed, return the cached result
            if key in dp:
                return dp[key]
            
            # If the characters at the current 'start' and 'end' are equal,
            # move inward by 1 position from both sides and solve the smaller problem
            if s[start] == s[end]:
                dp[key] = solve(start + 1, end - 1)
            else:
                # If the characters are different, we need to insert one character.
                # We either:
                # 1. Insert to match the character at 'end' (so move 'start' inwards),
                # 2. Insert to match the character at 'start' (so move 'end' inwards).
                # Add 1 insertion and take the minimum of both recursive solutions.
                dp[key] = 1 + min(solve(start + 1, end), solve(start, end - 1))

            # Return the computed result for the current range (start, end)
            return dp[key]
        
        # Call 'solve' on the entire string from the first character to the last.
        return solve()
