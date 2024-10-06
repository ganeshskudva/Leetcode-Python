class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Step 1: Create a mapping 'mp' where each character in 'order' is mapped to its index.
        # This allows us to compare words according to the alien dictionary order.
        # The dictionary 'mp' is constructed in O(26) = O(1) time, as there are at most 26 letters.
        mp = {c: i for i, c in enumerate(order)}
        
        # Step 2: Define a helper function 'is_bigger' that compares two words 's1' and 's2'.
        def is_bigger(s1, s2):
            # 'm' and 'n' are the lengths of the two words.
            m, n = len(s1), len(s2)
            
            # Step 3: Compare the two words character by character.
            # Iterate up to the length of the shorter word: O(min(m, n))
            for i in range(min(m, n)):
                # Step 4: If characters at the current position are different, we compare them using the alien dictionary order.
                if s1[i] != s2[i]:
                    # Return True if s1 > s2 in alien order, False otherwise.
                    return mp[s1[i]] > mp[s2[i]]
            
            # Step 5: If all characters compared so far are equal, the longer word is considered "bigger".
            # Return True if s1 is longer than s2 (i.e., s1 is lexicographically greater).
            return m > n
        
        # Step 6: Iterate through the list of words to check if they are in the correct order.
        # This loop runs (len(words) - 1) times: O(len(words))
        for i in range(1, len(words)):
            # Step 7: For each adjacent pair of words, check if the previous word is lexicographically greater than the next.
            # If it is, the list is not sorted, so return False.
            if is_bigger(words[i - 1], words[i]):
                return False
        
        # Step 8: If all words are in the correct order, return True.
        return True

# Time Complexity (TC):
# - Building the 'mp' dictionary takes O(26) = O(1) time as there are at most 26 letters in 'order'.
# - The 'is_bigger' function compares two words character by character, so it runs in O(min(m, n)) where m and n are the lengths of the two words being compared.
# - The outer loop iterates over all word pairs in the list, so it runs in O(len(words)).
# - Therefore, the overall time complexity is O(len(words) * average word length), which is O(n * k), where n is the number of words and k is the average word length.

# Space Complexity (SC):
# - The 'mp' dictionary requires O(26) = O(1) space for storing the character mappings.
# - The function uses constant space apart from the input, so space complexity is O(1) additional space.
# - The input list 'words' and string 'order' are not considered in space complexity as they are given as input.
# - Therefore, the space complexity is O(1).
