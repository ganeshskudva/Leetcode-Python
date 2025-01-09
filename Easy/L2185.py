class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([w for w in words if w.startswith(pref)])

# Time Complexity (TC): O(n * m), where n is the number of words in the list and m is the length of the prefix.
# For each word in the list, the startswith() function checks the prefix up to m characters.

# Space Complexity (SC): O(k), where k is the number of words matching the prefix. 
# The list comprehension creates a new list to store matching words.
