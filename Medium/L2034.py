import heapq

class StockPrice:

    def __init__(self):
        self.timestamps = {}  # Dictionary to store prices by timestamp
        self.highestTimestamp = 0  # Track the latest timestamp
        self.minHeap = []  # Min-heap to find the minimum price efficiently
        self.maxHeap = []  # Max-heap to find the maximum price efficiently (negate prices for max-heap)

    def update(self, timestamp: int, price: int) -> None:
        """
        Updates the price for the given timestamp.
        
        Time Complexity: O(log n), due to heap insertion for both minHeap and maxHeap.
        Space Complexity: O(n), for storing the timestamp-price pairs in the dictionary and the heaps.
        """
        self.timestamps[timestamp] = price
        self.highestTimestamp = max(self.highestTimestamp, timestamp)
        
        # Add the price to the heaps for min/max calculations
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))  # Negate price for max-heap behavior

    def current(self) -> int:
        """
        Returns the price at the latest timestamp.
        
        Time Complexity: O(1), since accessing the latest timestamp is direct.
        Space Complexity: O(1), no additional space is used.
        """
        return self.timestamps[self.highestTimestamp]

    def maximum(self) -> int:
        """
        Returns the maximum price recorded so far.
        
        Time Complexity: O(log n) in the worst case, as elements may need to be popped and pushed back onto the heap until a valid price is found.
        Space Complexity: O(1), no additional space is used beyond the temporary variables.
        """
        while self.maxHeap:
            currPrice, timestamp = heapq.heappop(self.maxHeap)
            if -currPrice == self.timestamps[timestamp]:  # Validate against the latest data
                heapq.heappush(self.maxHeap, (currPrice, timestamp))  # Push back the valid element
                return -currPrice

    def minimum(self) -> int:
        """
        Returns the minimum price recorded so far.
        
        Time Complexity: O(log n) in the worst case, as elements may need to be popped and pushed back onto the heap until a valid price is found.
        Space Complexity: O(1), no additional space is used beyond the temporary variables.
        """
        while self.minHeap:
            currPrice, timestamp = heapq.heappop(self.minHeap)
            if currPrice == self.timestamps[timestamp]:  # Validate against the latest data
                heapq.heappush(self.minHeap, (currPrice, timestamp))  # Push back the valid element
                return currPrice

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()