class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Convert a string to a 32-bit signed integer.

        Args:
        s (str): Input string.

        Returns:
        int: The integer representation of the string, clamped within the 32-bit signed integer range.

        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(1), as no extra space is used.
        """
        i, sign, base = 0, 1, 0
        max_int, min_int = 2**31 - 1, -2**31
        
        # Skip leading whitespaces
        s = s.lstrip()
        if not s:
            return 0

        # Check for sign
        if s[i] in "+-":
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Convert digits to integer
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow/underflow
            if base > max_int // 10 or (base == max_int // 10 and digit > 7):
                return max_int if sign == 1 else min_int
            
            base = base * 10 + digit
            i += 1

        return base * sign

# Time Complexity: O(n), where n is the length of the input string.
# Space Complexity: O(1), as the function uses constant space.
