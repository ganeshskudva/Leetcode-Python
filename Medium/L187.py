class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Initialize two sets:
        # 'seen' to track all the 10-character substrings we've encountered.
        # 'repeated' to track substrings that appear more than once.
        seen, repeated = set(), set()

        # Loop through the string `s`, stopping so that only valid 10-character substrings are considered.
        for i in range(len(s) - 9):
            # Extract a 10-character substring starting from index `i`.
            ten = s[i : i + 10]

            # If the substring has been seen before, add it to 'repeated'.
            if ten in seen:
                repeated.add(ten)

            # Add the substring to the 'seen' set to track it for future occurrences.
            seen.add(ten)

        # Convert the 'repeated' set to a list and return it, since the problem expects a list of repeated substrings.
        return list(repeated)

# Time Complexity (TC):
# The outer loop runs (n - 9) times, where `n` is the length of the string `s`. 
# For each substring of length 10, the operations of checking membership and adding elements to a set are O(1) on average.
# Therefore, the time complexity is O(n), where `n` is the length of the input string.

# Space Complexity (SC):
# We are using two sets, 'seen' and 'repeated', to store at most (n - 9) substrings of length 10. 
# The maximum number of distinct 10-character substrings is proportional to n.
# Therefore, the space complexity is O(n), where `n` is the length of the input string.
