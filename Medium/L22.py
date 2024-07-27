class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if not n:
            return res

        def solve(open_idx, close_idx, tmp=None):
            if tmp is None:
                tmp = []
            if len(tmp) == 2 * n:
                res.append(''.join(tmp))
                return

            if open_idx < n:
                tmp.append('(')
                solve(open_idx + 1, close_idx, tmp)
                del tmp[-1]

            if close_idx < open_idx:
                tmp.append(')')
                solve(open_idx, close_idx + 1, tmp)
                del tmp[-1]

        solve(0, 0)
        return res
