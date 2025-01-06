class Solution:
    def maxScore(self, s: str) -> int:
        # Count total ones in the string
        total_ones = s.count('1')
        zeroes, ones, maximum = 0, 0, float('-inf')

        # Iterate through the string except for the last character
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeroes += 1  # Increment zero count
            else:
                ones += 1  # Increment one count
            
            # Update the maximum score for the current split
            maximum = max(maximum, zeroes + (total_ones - ones))
        
        return maximum

# Time Complexity (TC):
# O(n), where n is the length of the string `s`. We perform a single pass through the string and use `s.count('1')` which also takes O(n).

# Space Complexity (SC):
# O(1), as we use a constant amount of extra space for variables like `zeroes`, `ones`, `total_ones`, and `maximum`.
