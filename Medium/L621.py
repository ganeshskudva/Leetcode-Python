import collections
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequency of each task using a Counter
        # Time Complexity: O(m), where m is the total number of tasks
        # Space Complexity: O(k), where k is the number of unique tasks
        freq = collections.Counter(tasks)
        
        # Step 2: Find the maximum frequency of any task
        # Time Complexity: O(k), iterating over unique task frequencies
        # Space Complexity: O(1), only a single integer is stored
        max_freq = max(freq.values())
        
        # Step 3: Count how many tasks have the maximum frequency
        # Time Complexity: O(k), iterating over unique task frequencies
        # Space Complexity: O(1), only a single integer is stored
        max_count = sum(1 for count in freq.values() if count == max_freq)
        
        # Step 4: Calculate the minimum intervals required based on the most frequent tasks
        # This calculation is done in constant time
        # Time Complexity: O(1), simple arithmetic calculation
        # Space Complexity: O(1), storing the integer result in `intervals`
        intervals = (max_freq - 1) * (n + 1) + max_count
        
        # Step 5: Return the maximum of the calculated intervals and the total number of tasks
        # Time Complexity: O(1), constant time for max comparison
        # Space Complexity: O(1), single integer for the final result
        return max(intervals, len(tasks))

# Overall Time Complexity: O(m + k), where m is the total number of tasks and k is the number of unique tasks.
# Overall Space Complexity: O(k), for storing the frequency of each unique task in the Counter.


import collections
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Handle edge case
        # If there are no tasks, return -1 as an indication of invalid input.
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        if not tasks:
            return -1
        
        # Step 2: Count frequency of each task and convert to a max heap (using negative values)
        # `collections.Counter(tasks).values()` creates a frequency dictionary, 
        # which we convert into a max heap to process the most frequent tasks first.
        # Time Complexity: O(m) to count tasks, where m is the number of tasks
        #                  O(k) to convert the list of frequencies to a heap, where k is unique tasks.
        # Space Complexity: O(k) for storing the frequencies of unique tasks in the heap.
        hp = [-f for f in collections.Counter(tasks).values()]
        heapq.heapify(hp)

        # Step 3: Initialize a counter to keep track of total intervals (time units) required.
        cnt = 0  # O(1) space

        # Step 4: Process tasks in intervals using a heap
        # Outer while loop runs until all tasks are scheduled (i.e., heap is empty).
        # Time Complexity: O(m log k), where m is the total number of tasks and k is unique tasks.
        while hp:
            interval, lst = n + 1, []  # Set interval size to `n + 1` for a full cycle
            
            # Inner loop: Process up to `n + 1` tasks in one interval (or cycle)
            # Each interval can include either tasks or idle time.
            # Time Complexity (per iteration): O(log k) for each `heapq.heappop()`
            while interval and hp:
                # Pop the task with the highest frequency from the heap
                freq = heapq.heappop(hp)
                
                # If this task has remaining instances, decrement frequency and store it in `lst`
                # Using `freq + 1` because `freq` is negative for max heap
                if freq < -1:
                    lst.append(freq + 1)
                
                # Decrease interval as we process each task or idle slot and increment count
                interval -= 1
                cnt += 1
            
            # Step 5: Re-add remaining tasks in `lst` (not fully processed) back to the heap
            # Time Complexity: O(log k) per insertion
            for freq in lst:
                heapq.heappush(hp, freq)
            
            # Step 6: If there are still tasks left in the heap, add idle time for remaining interval
            # If `interval > 0`, it means some slots were idle. We add those idle slots to `cnt`.
            # Time Complexity: O(1) to add remaining interval
            if hp:
                cnt += interval

        # Step 7: Return the total intervals (time units) required
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        return cnt

# Overall Complexity Summary:
# Time Complexity: O(m log k), where m is the total number of tasks and k is the number of unique tasks.
# Space Complexity: O(k), for storing the frequencies of unique tasks in the heap.


