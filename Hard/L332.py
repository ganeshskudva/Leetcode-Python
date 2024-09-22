from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # `flights` will store the adjacency list where each source has a list of destination airports
        # The list of destinations will be organized as a min-heap for each source
        flights = defaultdict(list)
        
        # `path` will store the final reconstructed itinerary
        path = []

        # Build the graph (adjacency list) from the tickets
        for src, dest in tickets:
            flights[src].append(dest)

        # Helper function to perform the DFS and construct the itinerary
        def solve(depart="JFK"):
            # Get the list of arrivals (destinations) for the current departure airport
            arrivals = flights[depart]
            
            # Convert the list of arrivals into a min-heap to ensure lexical order traversal
            heapq.heapify(arrivals)

            # While there are more destinations to visit from the current airport
            while arrivals:
                # Recursively visit the smallest lexicographical destination (heappop gets the smallest)
                solve(heapq.heappop(arrivals))

            # Once we are done with all destinations from `depart`, prepend it to the path
            # This ensures the path is built in reverse (post-order traversal) and gets corrected at the end
            path.insert(0, depart)
        
        # Start the DFS traversal from "JFK"
        solve()
        
        # Return the path which contains the lexicographically smallest itinerary
        return path
