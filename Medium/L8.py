class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        i, sign, base = 0, 1, 0
        max_int, min_int = 2**31 - 1, -2**31

        # Discard whitespaces in the beginning
        while i < len(s) and s[i] == ' ':
            i += 1

        # Check for sign
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Convert to integer and avoid overflow
        while i < len(s) and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            
            if base > (max_int // 10) or (base == max_int // 10 and digit > 7):
                return max_int if sign == 1 else min_int
            
            base = 10 * base + digit
            i += 1

        return base * sign
