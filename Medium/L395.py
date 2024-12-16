class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n, max_len = len(s), 0

        # Try all possible numbers of unique characters in the substring
        for target_unique in range(1, 27):
            # Frequency array to track occurrences of characters
            freq = [0] * 26
            i = j = unique = count_at_least_k = 0

            while j < n:
                # Expand the window
                if unique <= target_unique:
                    idx = ord(s[j]) - ord('a')
                    if freq[idx] == 0:
                        unique += 1  # Increment unique character count
                    freq[idx] += 1
                    if freq[idx] == k:
                        count_at_least_k += 1  # Increment valid character count
                    j += 1
                else:
                    # Shrink the window from the left
                    idx = ord(s[i]) - ord('a')
                    if freq[idx] == k:
                        count_at_least_k -= 1  # Decrement valid character count
                    freq[idx] -= 1
                    if freq[idx] == 0:
                        unique -= 1  # Decrement unique character count
                    i += 1

                # Update the maximum length if all conditions are satisfied
                if unique == target_unique and unique == count_at_least_k:
                    max_len = max(max_len, j - i)

        return max_len

# Time Complexity (TC):
# 1. Outer loop iterates over target_unique (1 to 26): O(26).
# 2. Inner loop expands and shrinks the window using two pointers, processing each character at most twice: O(n).
# Overall TC = O(26 * n) = O(n), since 26 is a constant.

# Space Complexity (SC):
# 1. Fixed size frequency array `freq` (size 26): O(26).
# 2. Other variables (pointers, counters) use O(1) space.
# Overall SC = O(1), since 26 is constant.
