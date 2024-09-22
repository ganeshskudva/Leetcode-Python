from heapq import *

class MedianFinder:

    def __init__(self):
        # min_heap stores the larger half of the numbers (min heap property: root is the smallest element)
        self.min_heap: List[int] = []
        
        # max_heap stores the smaller half of the numbers (max heap property: root is the largest element)
        # However, since Python's `heapq` is a min-heap by default, we store negative values to simulate a max-heap
        self.max_heap: List[int] = []
        

    def addNum(self, num: int) -> None:
        # First, add `num` to the `min_heap`. Then, pop the smallest element from `min_heap` 
        # and push it onto the `max_heap`. This ensures the max_heap always contains the smaller half.
        # Note: We push the negative value to simulate the behavior of a max heap.
        heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
        
        # If `max_heap` ends up with more elements than `min_heap`, we need to balance the heaps.
        # We pop the largest element from `max_heap` (remembering it's stored as negative, so we negate it),
        # and push it back to `min_heap`.
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        

    def findMedian(self) -> float:
        # Check if the total count of numbers is even. If so, the median is the average of the two middle elements.
        has_even_count = len(self.max_heap) == len(self.min_heap)

        if has_even_count:
            # The median is the average of the largest number from `max_heap` (the negative of the root)
            # and the smallest number from `min_heap` (the root of `min_heap`).
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        
        # If the total count of numbers is odd, the median is the smallest number in the `min_heap`
        # because we always ensure that `min_heap` will have one more element than `max_heap` in such cases.
        return float(self.min_heap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
