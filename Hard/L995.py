class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flipped = [False] * len(nums)
        valid_flip_times_from_past_window_for_current_idx = flip_cnt = 0
        for i in range(len(nums)):
            if i >= k:
                if flipped[i - k]:
                    valid_flip_times_from_past_window_for_current_idx -= 1
            
            if valid_flip_times_from_past_window_for_current_idx % 2 == nums[i]:
                if (i + k) > len(nums):
                    return -1
                valid_flip_times_from_past_window_for_current_idx += 1
                flipped[i] = True
                flip_cnt += 1
        
        return flip_cnt
