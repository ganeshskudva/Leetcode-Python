class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ret = [-1, -1]
        if len(nums) == 0:
            return ret
        
        def bs(start, first):
            lo, hi, mid, res = start, len(nums) - 1, 0, -1
            
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    if nums[mid] == target:
                        res = mid
                        if first:
                            hi = mid - 1
                        else:
                            lo = mid + 1
            
            return res
        
        ret[0] = bs(0, True)
        if ret[0] == -1:
            return ret
        
        ret[1] = bs(ret[0], False)
        
        return ret
