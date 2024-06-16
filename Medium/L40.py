class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def solve(start, tgt, tmp):
            if tgt < 0:
                return
            if tgt == 0:
                res.append(list(tmp))
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    tmp.append(candidates[i])
                    solve(i + 1, tgt - candidates[i], tmp)
                    del tmp[-1]
        
        candidates.sort()
        solve(0, target, [])
        return res
