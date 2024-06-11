class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        
        fast = 0
        while fast != slow:
            fast, slow = nums[fast], nums[slow]
        
        return slow
