class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        local_max, mx, partition_idx = nums[0], nums[0], 0
        for i in range(len(nums)):
            if local_max > nums[i]:
                local_max = mx
                partition_idx = i
            else:
                mx = max(mx, nums[i])

        return partition_idx + 1
