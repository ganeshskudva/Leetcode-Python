## heap 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Initialize the min-heap with intervals
        minHeap = intervals
        # Transform the list into a min-heap sorted by start time
        heapify(minHeap)
        
        # Result list to store merged intervals
        ans = []
        
        # While there are intervals in the min-heap
        while minHeap:
            # Pop the interval with the smallest start time
            start, end = heappop(minHeap)
            
            # Merge with overlapping intervals
            while minHeap and minHeap[0][0] <= end:
                # Update the end time if there's an overlap
                end = max(end, heappop(minHeap)[1])
            
            # Append the merged interval to the result list
            ans.append([start, end])
        
        return ans



## sorting
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Initialize result list
        res = []
        
        # Sort intervals by the start time
        intervals.sort(key=lambda x: x[0])

        # Iterate through each interval
        for i in intervals:
            # If result list is empty, add the first interval
            if not res:
                res.append(i)
            else:
                # If the current interval overlaps with the last one in result,
                # merge them by updating the end of the last interval in res
                if res[-1][1] >= i[0]:
                    res[-1][1] = max(res[-1][1], i[1])
                else:
                    # If there’s no overlap, simply append the current interval
                    res.append(i)

        return res

# Time Complexity (TC):
# - Sorting the intervals takes O(n log n), where n is the number of intervals.
# - After sorting, we perform a single pass through the intervals, which takes O(n).
# - Therefore, the overall time complexity is O(n log n) due to the sorting step.

# Space Complexity (SC):
# - The space complexity is O(n) for storing the merged intervals in the `res` list.
# - Sorting modifies the input list in-place, so no additional space is used for sorting.
# - Overall, the space complexity is O(n), as `res` may store up to all intervals in the worst case.

