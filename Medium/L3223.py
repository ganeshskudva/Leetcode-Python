class Solution:
    def minimumLength(self, s: str) -> int:
        from collections import Counter

        # Count the frequency of each character
        char_count = Counter(s)

        # Calculate the total characters to remove
        # For each character frequency, subtract all but the largest usable part
        to_remove = sum(f - 1 if f % 2 == 1 else f - 2 for f in char_count.values())

        # Return the minimum length of the string after removal
        return len(s) - to_remove

# Time Complexity (TC):
# - Counting frequencies with Counter(s): O(n), where n is the length of the string.
# - Summing over char_count.values(): O(k), where k is the number of unique characters.
# Overall: O(n + k), which simplifies to O(n) in the worst case where k <= n.

# Space Complexity (SC):
# - Counter object to store frequencies: O(k), where k is the number of unique characters.
# Overall: O(k).
