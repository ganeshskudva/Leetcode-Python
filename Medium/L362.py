class HitCounter:
    def __init__(self):
        """
        Initializes the HitCounter with a fixed-size counter (300 slots).
        Each slot stores a tuple (hits, timestamp) to track hit counts and the associated timestamp.
        """
        self.counter = [(0, 0)] * 300  # Initialize 300 slots (hits, timestamp)

    def hit(self, timestamp: int) -> None:
        """
        Records a hit at the specified timestamp.
        
        Parameters:
        timestamp (int): The time (in seconds) when the hit occurs.
        """
        idx = timestamp % 300  # Determine the index using modulo 300
        hits, ts = self.counter[idx]
        
        # If the stored timestamp doesn't match the current timestamp, reset the slot
        if ts != timestamp:
            self.counter[idx] = (1, timestamp)  # Set hit count to 1 with the current timestamp
        else:
            self.counter[idx] = (hits + 1, timestamp)  # Increment the hit count for the current timestamp

    def getHits(self, timestamp: int) -> int:
        """
        Returns the total number of hits in the last 300 seconds from the given timestamp.
        
        Parameters:
        timestamp (int): The current timestamp (in seconds).
        
        Returns:
        int: The total number of hits in the last 300 seconds.
        """
        total_hits = 0  # Initialize the total hit count

        # Iterate through all 300 slots to count valid hits within the 300-second window
        for hits, ts in self.counter:
            # Only count hits that occurred within the last 300 seconds
            if timestamp - ts < 300:
                total_hits += hits

        return total_hits