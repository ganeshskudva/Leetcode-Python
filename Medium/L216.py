class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def solve(start, tgt, tmp):
            if len(tmp) > k:
                return 
            if len(tmp) == k and not tgt:
                res.append(list(tmp))
            else:
                for i in range(start, 10):
                    tmp.append(i)
                    solve(i + 1, tgt - i, tmp)
                    del tmp[-1]
        
        solve(1, n, [])
        return res
