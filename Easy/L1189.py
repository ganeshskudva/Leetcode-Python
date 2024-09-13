class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        lst = ['b', 'a', 'l', 'o', 'n']
        cnt, mn = collections.Counter(text), float('inf')

        for c in lst:
            if c not in cnt:
                return 0
            if c == 'l' or c == 'o':
                mn = min(mn, cnt[c]//2)
            else:
                mn = min(mn, cnt[c])

        return 0 if mn == float('inf') else mn