import heapq
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Step 1: Combine start time, end time, and profit into a list of jobs as tuples (start, end, profit)
        # Then sort the jobs by their start time to process them in chronological order
        jobs = sorted(list(zip(startTime, endTime, profit)))

        # Initialize a priority queue (min-heap) to store jobs by their end time and cumulative profit
        pq = []
        
        # Initialize the total profit to 0
        total = 0
        
        # Step 2: Process each job one by one (s = start time, e = end time, p = profit)
        for s, e, p in jobs:
            # While there are jobs in the priority queue whose end time is less than or equal to the current job's start time
            # This means those jobs have already finished and can be considered for cumulative profit
            while pq and pq[0][0] <= s:
                # Remove the job with the earliest end time from the queue
                end, pro = heapq.heappop(pq)
                # Update the total profit to be the maximum profit we have seen so far
                total = max(total, pro)
            
            # Push the current job into the priority queue with its end time and its cumulative profit
            # The cumulative profit is the profit of the current job plus the best profit we've accumulated so far
            heapq.heappush(pq, (e, p + total))
        
        # Step 3: After processing all jobs, there may still be jobs in the priority queue
        # We need to ensure the maximum profit is taken from those jobs
        while pq:
            # Pop the remaining jobs and update the total profit with the maximum one
            end, pro = heapq.heappop(pq)
            total = max(total, pro)
        
        # Return the maximum profit after processing all jobs
        return total
