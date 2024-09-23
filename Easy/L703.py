from heapq import heappush, heappop
from typing import List

class KthLargest:

    # Initialize the KthLargest object with the value of k and an initial list of numbers
    def __init__(self, k: int, nums: List[int]):
        # Priority queue (min-heap) to store the k largest elements seen so far
        self.pq, self.k = [], k

        # Add all the numbers in the input list `nums` to the priority queue
        # This ensures that the priority queue only keeps track of the k largest numbers
        for n in nums:
            self.add(n)

    # Add a new value to the stream and return the k-th largest element
    def add(self, val: int) -> int:
        # Add the new value to the min-heap
        heappush(self.pq, val)

        # If the heap size exceeds k, remove the smallest element
        # This ensures the heap only contains the k largest elements
        if len(self.pq) > self.k:
            heappop(self.pq)

        # The smallest element in the min-heap is the k-th largest element
        return self.pq[0]
