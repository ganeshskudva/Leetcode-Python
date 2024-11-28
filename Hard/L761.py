class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Initialize balance counter and index
        cnt, idx = 0, 0
        # List to collect valid "special" substrings
        res = []

        # Iterate through the string
        for j, ch in enumerate(s):
            if ch == '1':
                cnt += 1  # Increment balance for '1'
            else:
                cnt -= 1  # Decrement balance for '0'

            # When balance is zero, we have a valid "special" substring
            if cnt == 0:
                # Recursively process the inner substring
                inner = self.makeLargestSpecial(s[idx+1:j])
                # Append the current "special" substring in correct format
                res.append(f"1{inner}0")
                idx = j + 1

        # Sort substrings only once at the top recursion level
        res.sort(reverse=True)

        # Join all substrings to form the final result
        return ''.join(res)

# Time Complexity (TC): O(n^2 log n)
# Explanation:
# - The outer loop runs O(n), where n is the length of the string.
# - For each valid "special" substring, a recursive call is made. In the worst case, there are O(n) recursive calls.
# - Sorting substrings at each recursion level takes O(k log k), where k is the number of substrings. Since k can be at most O(n), sorting takes O(n log n) at each recursive level.
# - Combining all factors, the overall complexity is O(n^2 log n).

# Space Complexity (SC): O(n^2)
# Explanation:
# - The recursion depth is proportional to the number of valid "special" substrings, which can be O(n) in the worst case.
# - Each recursive call processes a substring of size O(n), and space is required for storing substrings in `res`.
# - Hence, the total space complexity is O(n^2).
