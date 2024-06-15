class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_elem, cnt = nums[0], 1

        for i in range(1, len(nums)):
            if nums[i] == maj_elem:
                cnt += 1
            else:
                cnt -= 1
                if cnt <= 0:
                    maj_elem = nums[i]
                    cnt = 1

        return maj_elem 
