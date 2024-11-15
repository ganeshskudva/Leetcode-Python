class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Step 1: Identify the rightmost sorted subarray
        right = len(arr) - 1
        # Move 'right' backwards while the subarray from right to the end is sorted
        while right > 0 and arr[right-1] <= arr[right]:
            right -= 1
        
        # If the entire array is already sorted, no subarray needs to be removed
        if right == 0:
            return 0
        
        # Step 2: Initialize variables for the left pointer and the minimum result
        left, res = 0, right  # 'res' initialized to the size of the left unsorted part
        
        # Step 3: Extend the sorted left subarray
        while left < right and (left == 0 or arr[left-1] <= arr[left]):
            # Move 'right' forward to find a valid position where arr[left] <= arr[right]
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            # Calculate the minimum subarray length to remove
            res = min(res, right - left - 1)
            left += 1
        
        # Return the minimum length of the subarray to remove
        return res

        # Time Complexity (TC): O(n)
        # - The first while loop runs in O(n) as it traverses the array from right to left.
        # - The second while loop, along with the inner while loop, runs in O(n) amortized,
        #   as each element is processed at most twice.
        # - Overall TC: O(n)

        # Space Complexity (SC): O(1)
        # - The algorithm uses a constant amount of additional space for variables (`left`, `right`, `res`).
