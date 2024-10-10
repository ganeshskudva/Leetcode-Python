class Solution:
    def maxWidthRamp(self, A):
        n = len(A)
        
        # Step 1: Create rMax array where rMax[i] stores the maximum value from A[i] to A[n-1]
        rMax = [0] * n
        rMax[-1] = A[-1]
        
        # Populate rMax array by calculating the running maximum from right to left
        for i in range(n - 2, -1, -1):
            rMax[i] = max(rMax[i + 1], A[i])
        
        left = 0
        ans = 0
        
        # Step 2: Traverse the array using two pointers (left, right)
        for right in range(n):
            # Move the left pointer to the right while condition is not met
            while left < right and A[left] > rMax[right]:
                left += 1
            # Calculate maximum width ramp
            ans = max(ans, right - left)
        
        return ans

# Time Complexity (TC):
# - The first loop to create rMax takes O(n), where n is the length of the array A.
# - The second loop traverses the array with two pointers, also taking O(n).
# - Overall, the time complexity is O(n).

# Space Complexity (SC):
# - The space used for the rMax array is O(n).
# - No additional space apart from rMax and a few variables, so the overall space complexity is O(n).
