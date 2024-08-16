class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        
        def get_idx(c):
            return ord(c) - ord('A') + 1
        
        for c in columnTitle:
            res = (res * 26) + get_idx(c)
        
        return res
