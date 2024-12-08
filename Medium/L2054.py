from bisect import bisect_right
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort events by start time
        events.sort()  # O(n log n)

        # Step 2: Define a closure for solving the problem
        def solver():
            memo = {}  # To store results for (index, count) states

            def dp(index, count):
                # Base cases
                if count == 2:  # Maximum of two events can be picked
                    return 0
                if index >= len(events):  # No more events to pick
                    return 0

                # Check memoization
                if (index, count) in memo:
                    return memo[(index, count)]

                # Find the next event that starts after the current event's end time
                next_index = bisect_right(events, [events[index][1], float('inf'), float('inf')])  # O(log n)

                # Option 1: Pick the current event
                include = events[index][2] + dp(next_index, count + 1)

                # Option 2: Skip the current event
                exclude = dp(index + 1, count)

                # Save result in memo and return
                memo[(index, count)] = max(include, exclude)
                return memo[(index, count)]

            return dp

        # Step 3: Call the closure
        return solver()(0, 0)


# Time Complexity:
# - Sorting the events: O(n log n), where n is the number of events.
# - Binary search: For each recursive call, we perform a binary search (O(log n)) to find the next non-overlapping event.
# - Recursive calls: We make at most O(n) recursive calls, as we process each event once.
# - Total time complexity: O(n log n) for sorting + O(n log n) for recursion with binary search.
#   Hence, overall TC = O(n log n).

# Space Complexity:
# - Memoization: We store results for each (index, count) state in a dictionary. The total number of states is n * 2, so the space for memoization is O(n).
# - Recursion stack: In the worst case, the recursion depth can be O(n) (when we skip every event).
# - Total space complexity: O(n) for memoization + O(n) for recursion stack.
#   Hence, overall SC = O(n).
