class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        # Initialize variables:
        # max_len: stores the length of the longest subarray with equal elements
        # left: the left pointer for the sliding window
        # n: length of the nums array
        # cnt: a dictionary to store the count of each number in the current window
        max_len, left, n = 0, 0, len(nums)
        cnt = defaultdict(int)  # Default dictionary to count occurrences of each element in the window
        
        # Iterate over the array using the right pointer
        for right in range(n):
            # Increase the count of the current element at nums[right]
            cnt[nums[right]] += 1
            
            # max_len is updated to be the maximum frequency of any element in the current window
            max_len = max(max_len, cnt[nums[right]])
            
            # Calculate the current window length
            window_len = right - left + 1
            
            # If the window size minus the most frequent element's count exceeds k, 
            # it means there are more than 'k' replacements needed to make the subarray equal.
            if window_len - max_len > k:
                # Decrease the count of the element at the left pointer
                cnt[nums[left]] -= 1
                # Move the left pointer to the right to shrink the window
                left += 1
        
        # Return the length of the longest subarray with at most 'k' changes needed
        return max_len

# Time Complexity (TC):
# 1. We iterate through the entire 'nums' array once using the right pointer, which takes O(n).
# 2. Inside the loop, operations like updating the 'cnt' dictionary and finding the max frequency take O(1) time.
# 3. The left pointer moves at most 'n' times, but overall the sliding window ensures we only process each element once.
# Therefore, the overall time complexity is O(n), where 'n' is the length of the input array 'nums'.

# Space Complexity (SC):
# 1. The 'cnt' dictionary stores the frequency count of elements in the current window, which takes O(n) space in the worst case.
# 2. Additional variables like 'max_len', 'left', 'n', and 'window_len' take constant space O(1).
# Therefore, the overall space complexity is O(n), where 'n' is the length of the input array 'nums'.
