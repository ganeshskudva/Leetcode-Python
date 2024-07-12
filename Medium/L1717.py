class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a_cnt = b_cnt = res = 0
        lesser = min(x, y)
        
        for c in s:
            if c > 'b':
                res += min(a_cnt, b_cnt) * lesser
                a_cnt = b_cnt = 0
            elif c == 'a':
                if x < y and b_cnt:
                    b_cnt -= 1
                    res += y
                else:
                    a_cnt += 1
            else:
                if x > y and a_cnt:
                    a_cnt -= 1
                    res += x
                else:
                    b_cnt += 1
        
        res += min(a_cnt, b_cnt) * lesser
        return res
        
