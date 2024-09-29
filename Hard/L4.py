class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search performance.
        # If nums1 is larger, swap nums1 and nums2.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Lengths of the two arrays.
        m, n = len(nums1), len(nums2)
        
        # Initialize the binary search bounds: 'low' starts at 0, 'high' starts at the length of the smaller array (m).
        low, high = 0, m
        
        # Perform binary search to find the correct partition.
        while low <= high:
            # Partition X is the midpoint of nums1 based on the current 'low' and 'high' values.
            partitionX = (low + high) // 2
            
            # Partition Y is calculated so that the total number of elements to the left of partitionX and partitionY is equal.
            partitionY = (m + n + 1) // 2 - partitionX
            
            # Handle edge cases for the left and right sides of the partitions.
            # If partitionX is 0, it means there are no elements on the left side of nums1, so set maxX to negative infinity.
            # Otherwise, maxX is the element just before the partition in nums1.
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            
            # Similarly, if partitionY is 0, there are no elements on the left side of nums2, so set maxY to negative infinity.
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            
            # If partitionX is m, there are no elements on the right side of nums1, so set minX to positive infinity.
            # Otherwise, minX is the element just after the partition in nums1.
            minX = float('inf') if partitionX == m else nums1[partitionX]
            
            # Similarly, if partitionY is n, there are no elements on the right side of nums2, so set minY to positive infinity.
            minY = float('inf') if partitionY == n else nums2[partitionY]
            
            # Check if we have found the correct partition.
            # The correct partition is where the largest element on the left side is less than or equal to the smallest element on the right side.
            if maxX <= minY and maxY <= minX:
                # If the combined length of both arrays is even, the median is the average of the largest element on the left side
                # and the smallest element on the right side.
                if (m + n) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                # If the combined length is odd, the median is the largest element on the left side.
                else:
                    return max(maxX, maxY)
            
            # If the partition is not correct, adjust the binary search range:
            # If maxX > minY, move the partition in nums1 to the left (decrease 'high').
            elif maxX > minY:
                high = partitionX - 1
            # If maxY > minX, move the partition in nums1 to the right (increase 'low').
            else:
                low = partitionX + 1
