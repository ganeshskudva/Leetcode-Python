class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict to a set for faster lookups (O(1) average time complexity for set lookups)
        word_dict = set(wordDict)
        
        # Precompute and store the lengths of the words in wordDict, sorted in descending order.
        # This helps to try larger words first, potentially finding a solution faster.
        word_len = set(sorted((len(word) for word in wordDict), reverse=True))
        
        # Memoization dictionary to store the results of subproblems
        # mp[idx] will store whether the string from index `idx` to the end can be segmented
        mp = {}

        # Helper recursive function to solve the problem from a given index `idx`
        def solve(idx=0):
            # Base case: If we've reached the end of the string, return True
            if idx == len(s):
                return True
            
            # If we've already computed the result for this index, return the cached result
            if idx in mp:
                return mp[idx]

            # Try all word lengths in the word_dict (in descending order of length)
            for w in word_len:
                # Check if the substring from the current index `idx` to `idx + w` is a valid word
                if idx + w <= len(s) and s[idx: idx + w] in word_dict:
                    # If the substring is valid, recursively check the remainder of the string
                    if solve(idx + w):
                        # If a valid segmentation is found, store True in memoization dictionary and return
                        mp[idx] = True
                        return mp[idx]

            # If no valid segmentation is found, mark the current index as not solvable
            mp[idx] = False
            return mp[idx]

        # Start solving from index 0
        return solve()

# Time Complexity (TC):
# 1. Preprocessing the wordDict to create a set: O(K), where K is the total number of characters in all words in wordDict.
# 2. Sorting the word lengths takes O(M log M), where M is the number of words in wordDict.
# 3. The recursive function solve(idx) explores each index and checks all valid word lengths. In the worst case, it could explore all possible substrings at each index, 
#    leading to a time complexity of O(N^2), where N is the length of the string s.
# 4. Therefore, the overall time complexity is O(N^2 + K + M log M), dominated by O(N^2).

# Space Complexity (SC):
# 1. Memoization dictionary (mp) stores one result per index in the string, leading to a space complexity of O(N).
# 2. The recursion call stack has a maximum depth of O(N).
# 3. The word dictionary and word length set require space O(K + M), where K is the total number of characters in the dictionary and M is the number of words.
# 4. Therefore, the overall space complexity is O(N + K + M).
