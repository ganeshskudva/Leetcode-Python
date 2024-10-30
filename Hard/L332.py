class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # `flights` will store the adjacency list where each source has a list of destination airports
        # Space Complexity for `flights`: O(E), where E is the number of tickets (edges)
        # Each source has a list of destinations, stored as a min-heap to ensure lexical order.
        flights = defaultdict(list)
        
        # `path` will store the final reconstructed itinerary
        # Space Complexity for `path`: O(V), where V is the number of airports (nodes)
        # Path stores the itinerary of all visited nodes in reverse order initially
        path = []

        # Step 1: Build the graph (adjacency list) from the tickets
        # Time Complexity: O(E), as we process each ticket once to populate the adjacency list
        for src, dest in tickets:
            flights[src].append(dest)

        # Step 2: Define a helper function to perform DFS and construct the itinerary
        # This function uses recursive DFS traversal to visit each airport
        def solve(depart="JFK"):
            # Get the list of arrivals (destinations) for the current departure airport
            arrivals = flights[depart]
            
            # Convert the list of arrivals into a min-heap to ensure lexical order traversal
            # Time Complexity for heapify: O(d * log d), where d is the number of destinations from `depart`
            heapq.heapify(arrivals)

            # While there are more destinations to visit from the current airport
            # Total Time Complexity for all heappops: O(E log d), as we pop from the heap for each destination
            while arrivals:
                # Recursively visit the smallest lexicographical destination (heappop gets the smallest)
                solve(heapq.heappop(arrivals))

            # Once we are done with all destinations from `depart`, prepend it to the path
            # This ensures the path is built in reverse (post-order traversal) and gets corrected at the end
            path.insert(0, depart)  # O(V) in total as we insert each airport once

        # Step 3: Start the DFS traversal from "JFK"
        solve()
        
        # Step 4: Return the path which contains the lexicographically smallest itinerary
        # Time Complexity for returning the result: O(1)
        return path

# Overall Complexity Summary:
# Time Complexity: O(E log d), where E is the number of edges (tickets) and d is the average number of destinations per airport.
#                  This accounts for building the heap at each airport and popping elements.
# Space Complexity: O(V + E), where V is the number of nodes (airports) and E is the number of edges (tickets).
#                  We need O(V) space for the path and O(E) space for the adjacency list.

