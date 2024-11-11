# Reservoir Sampling
class Solution:

    def __init__(self, nums: List[int]):
        # Store the input array `nums` for reservoir sampling in `pick`
        # Space Complexity: O(N) for `nums`
        self.nums = nums

    def pick(self, target: int) -> int:
        # Perform reservoir sampling to find a random index of `target`
        count = 0
        chosen_index = -1
        
        # Time Complexity: O(N), where N is the length of nums
        for i, num in enumerate(self.nums):
            if num == target:
                # Increment the count of occurrences for `target`
                count += 1
                # Choose the current index with probability 1/count
                if random.randint(1, count) == 1:
                    chosen_index = i
        
        return chosen_index

# Time Complexity (TC):
# - Initialization (`__init__`): O(1), as we only store `nums` without any additional setup.
# - `pick` Method: O(N), where N is the length of `nums`, because we iterate through `nums` each time `pick` is called.

# Space Complexity (SC):
# - Initialization (`__init__`): O(N), as we store the `nums` array.
# - `pick` Method: O(1), as no additional space is used in this method.

# Dictionary of indices
class Solution:

    def __init__(self, nums: List[int]):
        # Initialize a dictionary to store indices of each number in nums
        # Space Complexity: O(N), where N is the length of nums
        self.mp = defaultdict(list)
        
        # Populate the dictionary with indices for each unique number in nums
        # Time Complexity: O(N)
        for i, n in enumerate(nums):
            self.mp[n].append(i)

    def pick(self, target: int) -> int:
        # Select a random index from the list of indices for the target number
        # Time Complexity: O(1) for selecting a random element
        return random.choice(self.mp[target])

# Time Complexity (TC):
# - Initialization (`__init__`): O(N), where N is the length of `nums`.
#   We iterate through `nums` once to populate `mp`.
# - `pick` Method: O(1), as we access the list of indices for `target` in `mp` and select a random element.

# Space Complexity (SC):
# - Initialization (`__init__`): O(N), as we store each index for each unique number in `nums` in `mp`.
# - `pick` Method: O(1), as no additional space is used in this method.

