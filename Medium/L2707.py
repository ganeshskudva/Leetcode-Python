class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dp will store the minimum extra characters needed for each index of string s
        # mp will act as a set of words from the dictionary for quick lookup
        dp, mp = defaultdict(int), Counter(dictionary)

        # Helper recursive function 'solve' that will calculate the minimum extra characters needed from index `idx`
        def solve(idx):
            # If idx goes beyond the length of the string, no more characters to process, return 0
            if idx >= len(s):
                return 0
            
            # If we already calculated the minimum extra characters for this index, return it (memoization)
            if idx in dp:
                return dp[idx]

            # Initialize variables:
            # min_extra keeps track of the minimum extra characters needed from index idx to the end
            # curr_extra holds the number of extra characters for the current substring
            min_extra, curr_extra = len(s), 0

            # Try every possible cut from index `idx` to the end of the string
            for cut_idx in range(idx, len(s)):
                # Get the current substring from idx to cut_idx
                curr = s[idx:cut_idx + 1]

                # If the current substring exists in the dictionary (mp), no extra characters are needed
                # Otherwise, the entire length of the substring is considered extra
                curr_extra = 0 if curr in mp else len(curr)

                # Recursively call solve to calculate the extra characters from the next position (cut_idx + 1)
                # Update min_extra with the minimum value between the current min_extra and the newly calculated one
                min_extra = min(min_extra, curr_extra + solve(cut_idx + 1))

            # Store the result in dp for future reference (memoization)
            dp[idx] = min_extra

            # Return the minimum extra characters needed from index `idx`
            return min_extra

        # Call the helper function starting from index 0
        return solve(0)