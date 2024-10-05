class Solution:
    def minFlips(self, s: str) -> int:
        """
        This function calculates the minimum number of flips required to make the binary string `s`
        into an alternating binary string (either starting with '0' or '1'). 
        
        Parameters:
        s (str): A binary string consisting of characters '0' and '1'.
        
        Returns:
        int: The minimum number of flips required to make the string alternate between '0' and '1'.
        """

        # Initialize the minimum number of flips to the length of the string.
        # This is the maximum number of flips possible (i.e., flipping every character).
        min_flips = len(s)

        # The window size `k` is the length of the original string.
        k = len(s)

        # If the string length is odd, double the string.
        # This allows us to handle the circular nature of the string more easily without explicitly
        # performing type-1 operations (i.e., rotating the string).
        # Example: '101' becomes '101101' to simulate rotation of bits.
        s = s if k % 2 == 0 else s + s

        # Since we are dealing with binary strings, there are only two possible valid alternating patterns:
        # 1. A string starting with '0' (e.g., 010101...).
        # 2. A string starting with '1' (e.g., 101010...).
        # We will compare the original string against these two patterns.

        # `altArr1` represents the alternating pattern starting with '0'.
        # `altArr2` represents the alternating pattern starting with '1'.
        altArr1, altArr2 = [], []
        for i in range(len(s)):
            altArr1.append("0" if i % 2 == 0 else "1")  # Pattern: 010101...
            altArr2.append("1" if i % 2 == 0 else "0")  # Pattern: 101010...

        # Convert the lists `altArr1` and `altArr2` into strings for easy comparison.
        alt1 = "".join(altArr1)
        alt2 = "".join(altArr2)

        # We will maintain two variables `diff1` and `diff2` to count the number of mismatches (flips needed)
        # between the current window of `s` and the alternating patterns `alt1` and `alt2`.
        diff1, diff2, left = 0, 0, 0  # `left` is the starting index of the sliding window.

        # Use a sliding window to traverse through the string `s` and compare each window of size `k` with `alt1` and `alt2`.
        for right in range(len(s)):
            # If the character at `right` in `s` does not match the corresponding character in `alt1`,
            # increment `diff1` (because a flip would be required to make them match).
            if s[right] != alt1[right]:
                diff1 += 1
            
            # Similarly, if the character at `right` in `s` does not match the corresponding character in `alt2`,
            # increment `diff2`.
            if s[right] != alt2[right]:
                diff2 += 1

            # Calculate the current window size.
            win_sz = right - left + 1

            # Once the window size reaches or exceeds `k`, we can start checking the number of flips required for that window.
            if win_sz >= k:
                # Update the minimum number of flips required by comparing the current window's `diff1` and `diff2`.
                # We are looking for the minimum number of flips needed to match either `alt1` or `alt2`.
                min_flips = min(min_flips, diff1, diff2)

                # Now, we slide the window to the right by shrinking it from the left:
                # If the character at `left` does not match `alt1`, decrement `diff1` as this character is leaving the window.
                if s[left] != alt1[left]:
                    diff1 -= 1
                
                # Similarly, update `diff2` if the character at `left` does not match `alt2`.
                if s[left] != alt2[left]:
                    diff2 -= 1
                
                # Move the `left` pointer to the right to shrink the window.
                left += 1

        # Return the minimum number of flips required.
        return min_flips
