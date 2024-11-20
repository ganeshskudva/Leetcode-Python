from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character in `s`.
        # Time Complexity: O(n), where n is the length of `s`.
        # Space Complexity: O(k), where k is the number of unique characters in `s`.
        mp = Counter(s)

        # Step 2: Create a bucket array to store characters by their frequencies.
        # Time Complexity: O(n), as the size of `tmp` is proportional to `len(s)`.
        # Space Complexity: O(n), as `tmp` has a length of len(s) + 1.
        tmp = [[] for _ in range(len(s) + 1)]
        for char, freq in mp.items():
            tmp[freq].append(char)

        # Step 3: Build the result by iterating over the bucket in reverse order.
        # Time Complexity: O(n), as we process each character proportional to its frequency.
        # Space Complexity: O(n), as `res` holds the output string characters.
        res = []
        for freq in range(len(tmp) - 1, 0, -1):
            for char in tmp[freq]:
                res.append(char * freq)  # Append the character `freq` times.

        # Step 4: Combine the result into a single string and return.
        # Time Complexity: O(n), for joining the string.
        return ''.join(res)

        # Overall Time Complexity: O(n), where n is the length of `s`.
        # Overall Space Complexity: O(n), including `tmp` and `res`.
