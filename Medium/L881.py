class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Initialize the boat count and pointers for the two-pointer approach
        boat_cnt = 0  # This will keep track of the number of boats required
        left = 0  # Pointer for the lightest person (start of the list)
        right = len(people) - 1  # Pointer for the heaviest person (end of the list)

        # Edge case: if the list is empty, return 0 boats
        if not people:
            return boat_cnt
        
        # Sort the list of people by their weight
        people.sort()
        
        # Use a two-pointer approach to pair the lightest and heaviest person
        while left <= right:
            # Calculate the total weight of the lightest and heaviest person
            tot = people[left] + people[right]
            
            # If their combined weight is less than or equal to the limit,
            # they can share the same boat, so move the left pointer
            if tot <= limit:
                left += 1  # Move the left pointer to the next lightest person

            # Always move the right pointer to put the heaviest person on a boat
            boat_cnt += 1  # Increment the boat count, as a boat is used
            right -= 1  # Move the right pointer to the next heaviest person
        
        # Return the total number of boats needed
        return boat_cnt

# Time Complexity (TC): 
# - Sorting the people list takes O(n log n), where n is the number of people.
# - The while loop runs at most n times (left and right pointers traverse the list once).
# - Overall time complexity is O(n log n) due to the sorting step.

# Space Complexity (SC): 
# - Sorting the list uses O(n) extra space for storing the sorted people.
# - No additional data structures are used that grow with input size, so the space complexity is O(n).
