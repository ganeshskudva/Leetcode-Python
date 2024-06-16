class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates:
            return res
        
        def solve(idx, tgt, tmp):
            if tgt < 0 or idx > len(candidates):
                return 
            if not tgt:
                res.append(list(tmp))
            
            for i in range(idx, len(candidates)):
                tmp.append(candidates[i])
                solve(i, tgt - candidates[i], tmp)
                del (tmp[-1])
        
        solve(0, target, [])
        return res
