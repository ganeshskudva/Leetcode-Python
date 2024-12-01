class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # Dictionary mapping for strobogrammatic digits
        kv = {
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6',
            '0': '0'
        }

        # Two pointers: one starting from the beginning, the other from the end
        left, right = 0, len(num) - 1

        while left <= right:
            # Check if both digits are valid and their mapping matches
            if num[left] not in kv or num[right] not in kv or kv[num[left]] != num[right]:
                return False
            # Move the pointers closer
            left += 1
            right -= 1

        return True

# Time Complexity (TC): O(n), where n is the length of the input string `num`.
# This is because we iterate through each digit at most once.

# Space Complexity (SC): O(1).
# The optimized approach uses constant space as no additional data structures are used apart from the dictionary.
