class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        def rotation_cnt():
            l, r = 0, len(nums) - 1

            while l < r:
                mid = (l + r) // 2
                if mid < r and nums[mid] > nums[mid + 1]:
                    return mid + 1
                if mid > l and nums[mid] < nums[mid - 1]:
                    return mid
                if nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return l
        
        rot_cnt = rotation_cnt()
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            real_mid = (mid + rot_cnt) % len(nums)
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
