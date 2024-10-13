class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Step 1: Initialize a min-heap (priority queue) with the first element of each list.
        # Each entry in the heap is a tuple (value, list_index, element_index).
        # The heap helps us keep track of the smallest current value across all lists.
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        
        # Step 2: Convert the list `pq` into a valid heap in O(k) time, where `k` is the number of lists.
        heapq.heapify(pq)

        # Step 3: Initialize the result range (ans) with very large negative and positive values.
        # This will be used to track the smallest range found so far.
        ans = -1e9, 1e9

        # Step 4: Set `right` to the largest first element from all lists.
        # This will help define the current range [left, right] as we extract values from the heap.
        right = max(row[0] for row in nums)

        # Step 5: Start the process of extracting the smallest element (left) from the heap,
        # and try to update the smallest range [left, right] found so far.
        while pq:
            left, i, j = heapq.heappop(pq)  # Extract the smallest element from the heap.
            
            # Step 6: Update the current best range if the current range [left, right] is smaller than the best range.
            if right - left < ans[1] - ans[0]:
                ans = left, right  # Update the best range with [left, right].

            # Step 7: If the extracted element is the last element from its list, we stop.
            # This is because we can't extend the range further for this list.
            if j + 1 == len(nums[i]):
                return list(ans)  # Convert the range into a list and return it as the result.

            # Step 8: If there are more elements in the current list, add the next element to the heap.
            v = nums[i][j + 1]
            right = max(right, v)  # Update `right` to the maximum value in the current range.
            
            # Step 9: Push the next element (v, i, j + 1) into the heap. 
            # `v` is the next element in the current list, `i` is the list index, and `j + 1` is the new element index.
            heapq.heappush(pq, (v, i, j + 1))

# Time Complexity (TC):
# 1. Building the heap initially takes O(k) time, where `k` is the number of lists (since we are heapifying the first elements of each list).
# 2. The while loop runs as long as there are elements in the heap. In the worst case, each element from each list is pushed and popped from the heap.
#    - Pushing and popping from a heap takes O(log k) time, where `k` is the number of lists.
#    - Since there are `N` total elements across all lists, and each one is inserted and removed from the heap, 
#      the total time for heap operations is O(N log k).
# 3. Finding the maximum first element across the lists takes O(k) at the start.

# Therefore, the overall time complexity is O(N log k), where `N` is the total number of elements across all lists and `k` is the number of lists.

# Space Complexity (SC):
# 1. The heap stores up to `k` elements at any time, where `k` is the number of lists.
# 2. We also store variables such as `right`, `ans`, and a few others, but these require constant space.
# 3. The total space used by the heap is O(k), and the additional space used by other variables is O(1).

# Therefore, the overall space complexity is O(k), where `k` is the number of lists.