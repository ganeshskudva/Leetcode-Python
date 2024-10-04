class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # n: the length of the input list 'nums'
        # beg, end: indices that will track the beginning and end of the subarray that needs to be sorted
        # mn: the minimum value encountered from the right end of the list
        # mx: the maximum value encountered from the left end of the list
        n, beg, end, mn, mx = len(nums), -1, -2, nums[-1], nums[0]

        # Traverse the list once, updating mx (max value) from left to right and mn (min value) from right to left.
        for i in range(1, n):
            # mx is the maximum value we've encountered so far from the left side (index 0 to i)
            mx = max(mx, nums[i])
            # mn is the minimum value we've encountered so far from the right side (index n-1 to n-i-1)
            mn = min(mn, nums[n - 1 - i])
            
            # If the current number is smaller than the maximum encountered so far, 
            # it means this element is out of order, and we update 'end'.
            if nums[i] < mx:
                end = i
            
            # If the current number from the right is larger than the minimum encountered so far,
            # it means this element is out of order, and we update 'beg'.
            if nums[n - 1 - i] > mn:
                beg = n - 1 - i

        # The result is the length of the unsorted subarray, which is calculated as end - beg + 1.
        # If no unsorted subarray is found, the return will be 0 (because beg will remain greater than end).
        return end - beg + 1
