from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Step 1: Attach index to each task and sort by enqueue time
        tasks = sorted([(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))])

        result = []           # List to store the order of task indices
        min_heap = []         # Min-heap to store available tasks based on processing time
        time = 0              # Current time
        i = 0                 # Index to traverse sorted tasks list
        
        # Step 2: Process all tasks
        while i < len(tasks) or min_heap:
            # Add all tasks whose enqueue time <= current time to the heap
            while i < len(tasks) and tasks[i][0] <= time:
                # Push (processing time, index) to maintain min-heap by processing time
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if min_heap:
                # Pop the task with the smallest processing time
                proc_time, index = heapq.heappop(min_heap)
                result.append(index)   # Append task index to result
                time += proc_time      # Increment time by the task's processing time
            else:
                # If no tasks are available, jump time to the next task's enqueue time
                time = tasks[i][0]

        return result

# Overall Time Complexity: O(n log n)
#   - Sorting the tasks initially takes O(n log n).
#   - Each task is pushed and popped from the heap once, each operation taking O(log n).

# Overall Space Complexity: O(n)
#   - We store tasks in `tasks`, `result`, and in the `min_heap`, each of which can hold up to n elements.
