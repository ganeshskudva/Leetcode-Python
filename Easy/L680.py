class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid_palindrome(s):
            return s == s[::-1]

        i,j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i, j = i + 1, j - 1
            else:
                return valid_palindrome(s[i+1:j+1]) or valid_palindrome(s[i:j])
        
        return True
