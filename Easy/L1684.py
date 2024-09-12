class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow_st, cnt = set(allowed), 0

        for w in words:
            if set(w) <= allow_st:
                cnt += 1

        return cnt
