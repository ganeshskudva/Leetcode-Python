class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        # Sort both lists of slots by the start time (default behavior)
        slots1.sort()
        slots2.sort()
        i = 0
        j = 0
        
        # Use two pointers to iterate through both sorted lists
        while i < len(slots1) and j < len(slots2):
            # Calculate the overlap interval between slots1[i] and slots2[j]
            head = max(slots1[i][0], slots2[j][0])
            tail = min(slots1[i][1], slots2[j][1])
            
            # Check if the overlapping interval is at least `duration`
            if head + duration <= tail:
                return [head, head + duration]
            
            # Move the pointer for the slot that ends earlier to find a potential larger overlap
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        
        # Return an empty list if no common interval of sufficient duration is found
        return []

# Time Complexity (TC): O(n log n + m log m)
#   - Sorting both `slots1` and `slots2` by start time takes O(n log n) and O(m log m), where n and m are their lengths.
#   - After sorting, we perform a single pass through both lists using two pointers, which takes O(n + m).
#   - Thus, the overall time complexity is dominated by the sorting steps, resulting in O(n log n + m log m).

# Space Complexity (SC): O(1)
#   - Sorting is performed in place, so no additional space is needed for sorting.
#   - Only a constant amount of extra space is used for the two pointers (i, j) and auxiliary variables (head, tail).
#   - Therefore, the space complexity is O(1).
