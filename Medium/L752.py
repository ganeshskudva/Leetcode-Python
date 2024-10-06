from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Helper function to generate all possible neighboring states for a given lock state.
        # Time complexity of neighbors function: O(1) because it generates 8 neighbors for each lock state.
        # Space complexity of neighbors function: O(1) for the temporary list to store 8 neighbors.
        def neighbors(code):
            result = []  # List to store all neighbors
            for i in range(4):  # There are 4 wheels on the lock
                x = int(code[i])  # Get the current digit of the lock at position 'i'
                
                # Generate two neighbors by rotating the wheel by -1 and +1
                for diff in (-1, 1):
                    # Using (x + diff + 10) % 10 to handle wrapping from 9 to 0 and 0 to 9.
                    y = (x + diff + 10) % 10  
                    
                    # Create a new lock combination by replacing the digit at position 'i'
                    new_code = code[:i] + str(y) + code[i + 1:]
                    
                    # Add the new combination to the result list
                    result.append(new_code)
                    
            return result  # Return the list of all possible lock combinations

        # Convert deadends to a set for faster lookup, since set lookups are O(1) on average
        # Time complexity: O(d), where d is the number of deadends.
        # Space complexity: O(d), because we store all deadends in a set.
        deadSet = set(deadends)

        # If the initial state "0000" is in the deadends, return -1 as it's impossible to start
        if "0000" in deadSet: 
            return -1
        
        # Initialize BFS queue with the starting position "0000"
        # Time complexity for deque operations (popleft and append) is O(1) on average.
        q = deque(["0000"])
        
        # This keeps track of the number of steps taken to unlock the lock
        steps = 0

        # Perform BFS until we process all possible combinations or find the solution
        # Time complexity of BFS: O(10^4) in the worst case, as there are 10^4 possible lock combinations.
        # Space complexity of BFS: O(10^4) for the queue and the visited set, as at most 10^4 combinations can be stored.
        while q:
            # Process all combinations at the current BFS level (i.e., all combinations reached in 'steps' moves)
            for _ in range(len(q)):
                # Pop the next combination to be processed from the front of the queue
                curr = q.popleft()
                
                # If the current combination matches the target, return the number of steps taken
                if curr == target:
                    return steps
                
                # Generate all valid neighbor combinations and process them
                for nei in neighbors(curr):
                    # If the neighbor is in deadends, skip it
                    if nei in deadSet:
                        continue
                    
                    # Mark this neighbor as visited by adding it to deadSet
                    # (We use deadSet for visited to avoid revisiting and to prevent infinite loops)
                    deadSet.add(nei)
                    
                    # Add the valid neighbor to the BFS queue for processing in the next steps
                    q.append(nei)
            
            # Increment the step count after processing all combinations at the current level
            steps += 1

        # If we exhaust all possibilities and do not find the target, return -1
        return -1

