class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize two pointers: 'lo' at the start and 'hi' at the end of the array.
        lo, hi = 0, len(arr) - 1
        
        # The loop will run until the window of 'k' elements is found.
        # At each step, we shrink the range [lo, hi] by either moving 'lo' or 'hi'.
        while hi - lo >= k:
            # Compare the absolute difference between the element at 'lo' and 'x'
            # with the absolute difference between the element at 'hi' and 'x'.
            if abs(arr[lo] - x) > abs(arr[hi] - x):
                # If the element at 'lo' is farther from 'x' than the element at 'hi',
                # move the 'lo' pointer to the right (narrowing the range).
                lo += 1
            else:
                # If the element at 'hi' is farther from 'x' or they are equally distant,
                # move the 'hi' pointer to the left (narrowing the range).
                hi -= 1
        
        # Return the subarray of 'k' closest elements. The range is [lo, hi] inclusive.
        return arr[lo:hi+1]
