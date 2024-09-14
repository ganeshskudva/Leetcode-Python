class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Initialize 'flights' as a defaultdict of lists to store the adjacency list for the graph.
        # 'path' will hold the final itinerary.
        flights, path = defaultdict(list), []

        # Construct the graph by iterating through the tickets.
        for src, dest in tickets:
            # For each ticket, add the destination to the list of flights from the source.
            flights[src].append(dest)

        # The DFS helper function to construct the itinerary.
        def solve(depart="JFK"):
            # Get the list of destinations (arrivals) from the current departure airport.
            arrivals = flights[depart]
            
            # Convert the list of arrivals into a min-heap to ensure lexicographical order.
            heapq.heapify(arrivals)

            # While there are still available destinations from the current airport
            while arrivals:
                # Recursively visit the lexicographically smallest destination
                solve(heapq.heappop(arrivals))

            # Once all destinations from this airport are visited, insert the airport at the start of the path.
            # This is a key part of the post-order DFS traversal that ensures the path is built in reverse.
            path.insert(0, depart)
        
        # Start the DFS from "JFK", which is always the starting point.
        solve()
        
        # Return the final path (itinerary) in the correct order.
        return path
