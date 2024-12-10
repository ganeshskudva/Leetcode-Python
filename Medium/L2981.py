from collections import Counter

class Solution:
    def maximumLength(self, s: str) -> int:
        # List to store all possible contiguous substrings
        subarrays = []

        # Generate all contiguous substrings of characters
        for i in range(len(s)):
            index = i
            # Extend the substring as long as the current character repeats
            while index < len(s) and s[index] == s[i]:
                subarrays.append(s[i:index + 1])  # Append the substring
                index += 1

        # Count occurrences of each substring
        counter = Counter(subarrays)

        # Variable to track the maximum valid substring length
        max_len = 0

        # Iterate through the counted substrings
        for j, n in counter.items():
            # If the substring occurs at least 3 times, check its length
            if n >= 3:
                if len(j) > max_len:
                    max_len = len(j)

        # If no valid substring found, return -1
        if max_len == 0:
            return -1

        # Return the maximum length
        return max_len

# Time Complexity (TC):
# 1. Outer loop to iterate over the string: O(n)
# 2. Inner `while` loop to generate substrings: Worst-case O(n^2)
#    - For each character, you generate all contiguous substrings, which can be quadratic.
# 3. Creating the `Counter` object: O(k), where k is the number of unique substrings.
# 4. Iterating through the `counter.items()`: O(k).
# Overall TC: O(n^2 + k), but since k depends on n (e.g., in the worst case, all substrings are unique), it simplifies to **O(n^2)**.

# Space Complexity (SC):
# 1. Storing all substrings in `subarrays`: Worst-case O(n^2) (e.g., for "aaaa", you generate n(n+1)/2 substrings).
# 2. `Counter` object storage: O(k), where k is the number of unique substrings.
# Overall SC: **O(n^2)** in the worst case due to substring storage.
