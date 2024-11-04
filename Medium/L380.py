import random

class RandomizedSet:

    def __init__(self):
        # Dictionary to store element index mappings
        self.mp = {}
        # List to store the elements
        self.nums = []

    def insert(self, val: int) -> bool:
        # Check if val is already present
        if val in self.mp:
            return False
        # Append val to the list and store its index in the dictionary
        self.nums.append(val)
        self.mp[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        # Check if val is present in the set
        if val not in self.mp:
            return False
        # Get the last element in the list and the index of the element to be removed
        last_val = self.nums[-1]
        idx_to_remove = self.mp[val]
        # Move the last element to the index of the element to be removed
        self.nums[idx_to_remove] = last_val
        self.mp[last_val] = idx_to_remove
        # Remove the last element from the list and the val from the dictionary
        self.nums.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.nums)

# Time Complexity:
# - insert: O(1)
# - remove: O(1)
# - getRandom: O(1)

# Space Complexity:
# - O(N), where N is the number of elements in the set
