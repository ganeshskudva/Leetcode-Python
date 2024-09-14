class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict to a set for fast lookups
        word_set = set(wordDict)
        # Memoization to store results for each index
        memo = {}
        # Cache the lengths of words in wordDict to avoid unnecessary string slicing
        word_lens = set(len(word) for word in wordDict)

        def solve(idx):
            # If we reach the end of the string, return True
            if idx == len(s):
                return True
            
            # If we've already computed this subproblem, return the cached result
            if idx in memo:
                return memo[idx]

            # Try to find a valid word break starting from index 'idx'
            for length in word_lens:
                # Ensure the current word doesn't exceed the bounds of the string
                if idx + length <= len(s):
                    substring = s[idx:idx + length]
                    # If the substring is a valid word, attempt to solve the rest of the string
                    if substring in word_set:
                        # Early exit if the rest of the string can be segmented
                        if solve(idx + length):
                            memo[idx] = True
                            return True

            # If no valid segmentation is found, store the result as False
            memo[idx] = False
            return False

        # Start solving from index 0
        return solve(0)
