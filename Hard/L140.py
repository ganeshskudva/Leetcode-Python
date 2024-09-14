class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Convert the wordDict to a set for O(1) lookups
        word_set = set(wordDict)
        
        # Memoization map to store results of subproblems (start index -> list of sentences)
        memo = defaultdict(list)

        # Helper function to recursively break the string from the given start index
        def solve(start):
            # If we already have the result for this start index, return it
            if start in memo:
                return memo[start]
            
            # Base case: if we've reached the end of the string, return a list with an empty string
            if start == len(s):
                return [""]

            # List to store all valid sentences starting from 'start'
            res = []
            
            # Try all words in the dictionary to see if they match the current substring
            for word in word_set:
                # Only check if the current substring can start with this word
                word_len = len(word)
                
                # Check if the word can fit into the remaining part of the string
                if start + word_len <= len(s) and s[start:start + word_len] == word:
                    # Recursively solve the remaining string after the word
                    sub_res = solve(start + word_len)
                    
                    # For each result from the recursive call, combine with the current word
                    for sub in sub_res:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)  # No need to add a space if this is the last word

            # Memoize the result for this start index to avoid recomputation
            memo[start] = res
            return res

        # Start the recursive process from index 0
        return solve(0)