import random
from collections import defaultdict

class RandomizedSet:

    def __init__(self):
        # Dictionary to store element index mappings
        self.mp = defaultdict(int)
        # List to store the elements
        self.nums = []

    def insert(self, val: int) -> bool:
        # Check if val is already present
        if val in self.mp:
            return False
        # Append val to the list and update its index in the dictionary
        self.nums.append(val)
        self.mp[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        # Check if val is present in the set
        if val not in self.mp:
            return False
        # Replace the element to be removed with the last element
        if self.mp[val] < len(self.nums) - 1:
            last_val = self.nums[-1]
            self.nums[self.mp[val]] = last_val
            self.mp[last_val] = self.mp[val]
        # Remove the last element from the list
        self.nums.pop()
        # Remove val from the dictionary
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        # Return a random element from the list
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Time Complexity (TC):
# - insert: O(1), as we add to the end of the list and update the dictionary.
# - remove: O(1), as we swap and remove the last element from the list and update the dictionary.
# - getRandom: O(1), as we access a random element by index in the list.

# Space Complexity (SC):
# - O(N), where N is the number of elements in the set, as both the dictionary and list store up to N elements.
