class Solution:
    def countDigitOne(self, n: int) -> int:
        st, mp = str(n), {}
        
        def solve(idx, tight, count):
            if idx == len(st):
                return count
            
            key = "%d-%d-%d" % (idx, tight, count)
            if key in mp:
                return mp[key]
            
            ans, bound = 0, 9
            if tight == 1:
                bound = ord(st[idx]) - ord('0')
            
            for i in range(bound + 1):
                add = 0
                if i == 1:
                    add = 1
                
                ans += solve(idx + 1, 1, count + add) if i == bound and tight == 1 else solve(idx + 1, 0, count + add)
        
            mp[key] = ans
            return ans
        
        return solve(0, 1, 0)
