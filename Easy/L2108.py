class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_pal(s):
            return s == s[::-1]
        for w in words:
            if is_pal(w):
                return w
        
        return ""
