class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def solve(st):
            c, arr = 0, [''] * len(st)
            for i in range(len(st)):
                if st[i] == '#':
                    c -= 1
                    c = max(0, c)
                else:
                    arr[c] = st[i]
                    c += 1
            return ''.join(arr)[:c]
        return solve(s) == solve(t)
