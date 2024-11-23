class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Step 1: Count occurrences of each character in `s`.
        arr = [0] * 26
        for ch in s:
            arr[ord(ch) - ord('a')] += 1

        # Step 2: Build the result string by processing `order` and remaining characters.
        result = []
        for ch in order:
            idx = ord(ch) - ord('a')
            if arr[idx] > 0:  # Skip characters not in `s`
                result.append(ch * arr[idx])
                arr[idx] = 0

        # Append remaining characters not in `order`.
        for i in range(26):
            if arr[i] > 0:
                result.append(chr(i + ord('a')) * arr[i])

        # Step 3: Combine the result into a single string and return.
        return ''.join(result)

# Time Complexity:
#   - Counting characters in `s`: O(n), where n is the length of `s`.
#   - Processing `order`: O(m), where m is the length of `order`.
#   - Processing remaining characters: O(26) = O(1) (fixed size for English alphabet).
#   - Joining the result string: O(k), where k is the length of the result.
#   - Total: O(n + m + k).

# Space Complexity:
#   - Fixed array `arr` of size 26: O(1).
#   - `result` list (output): O(k), where k is the length of the result string.
#   - Total: O(k) (output space doesn't count as extra space).
