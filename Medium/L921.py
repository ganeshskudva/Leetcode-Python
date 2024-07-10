class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st_size = mismatch = 0
        
        for c in s:
            if c == '(':
                st_size += 1
            elif c == ')' and st_size:
                st_size -= 1
            else:
                mismatch += 1
        
        return st_size + mismatch
