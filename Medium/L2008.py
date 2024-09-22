from heapq import heappop, heappush

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # Sort the rides by their start time (to process them in chronological order)
        rides.sort()
        
        # Priority queue (min-heap) to store rides by their end time along with the cumulative earnings
        hp = []
        
        # `tot` keeps track of the maximum total earnings accumulated so far
        tot = 0
        
        # Iterate through each ride in the sorted list
        for s, e, t in rides:  # s = start, e = end, t = tip
            # Process all the rides that end before or at the current ride's start time
            # We can finish these rides before starting the current ride
            while hp and s >= hp[0][0]:  # hp[0][0] is the earliest end time in the heap
                _, tips = heappop(hp)  # Pop the ride that ends earliest
                # Update `tot` to be the maximum earnings we've seen so far (including this ride's earnings)
                tot = max(tot, tips)
            
            # Push the current ride's end time and cumulative earnings into the heap
            # The cumulative earnings are calculated as the earnings from this ride (distance + tip) plus `tot`
            heappush(hp, (e, e - s + t + tot))  # e - s is the fare, t is the tip, `tot` is previous max earnings
        
        # After processing all rides, there may still be rides in the heap that haven't been considered yet.
        # We process them here to make sure we get the maximum earnings possible.
        while hp:
            _, tips = heappop(hp)  # Pop each remaining ride in the heap
            # Update `tot` to capture the maximum earnings possible
            tot = max(tot, tips)
        
        # Return the maximum total earnings possible after considering all rides
        return tot
