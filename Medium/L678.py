class Solution:
    def checkValidString(self, s: str) -> bool:
        c_min, c_max = 0, 0
        
        for c in s:
            if c == '(':
                c_max, c_min = c_max + 1, c_min + 1
            elif c == ')':
                c_max, c_min = c_max - 1, c_min - 1
            elif c == '*':
                c_max, c_min = c_max + 1, c_min - 1
            
            if c_max < 0:
                return False
            
            c_min = max(c_min, 0)
            
        return c_min == 0
