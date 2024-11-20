class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Step 1: Calculate the minimum number of each character ('a', 'b', 'c') 
        # that needs to remain after removal.
        limits = {c: s.count(c) - k for c in 'abc'}
        
        # If any character count is less than `k`, return -1 as it's not possible.
        if any(x < 0 for x in limits.values()):
            return -1

        # Step 2: Sliding window to find the maximum possible length of the valid substring.
        cnts = {c: 0 for c in 'abc'}
        ans = l = 0  # `ans` stores the maximum length, `l` is the left pointer.

        # Traverse the string with a right pointer `r`.
        for r, c in enumerate(s):
            cnts[c] += 1
            # Adjust the left pointer `l` to ensure the substring respects `limits`.
            while cnts[c] > limits[c]:
                cnts[s[l]] -= 1
                l += 1
            # Update the maximum length of the valid substring.
            ans = max(ans, r - l + 1)

        # Step 3: Calculate the minimum number of characters to remove.
        return len(s) - ans

        # Time Complexity: O(n), where n is the length of the string `s`.
        # Space Complexity: O(1), as only fixed-size dictionaries are used.
