class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early return if the lengths of the strings are different.
        # If they have different lengths, they can't be anagrams.
        if len(s) != len(t):
            return False
        
        # Initialize a list of size 26 to count character occurrences.
        # We assume the input consists of lowercase English letters.
        count = [0] * 26
        
        # Iterate over both strings simultaneously.
        for i in range(len(s)):
            # Increment the count for the character in 's'.
            count[ord(s[i]) - ord('a')] += 1
            # Decrement the count for the character in 't'.
            count[ord(t[i]) - ord('a')] -= 1
        
        # If the counts for all characters are zero, the strings are anagrams.
        # If any count is non-zero, return False.
        return all(x == 0 for x in count)