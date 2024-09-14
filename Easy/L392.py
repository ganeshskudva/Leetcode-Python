class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) > len(t):
            return False

        sp, tp = 0,0
        count = 0
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
                count += 1
            elif s[sp] != t[tp]:
                tp += 1
            
        if count == len(s):
            return True
        return False