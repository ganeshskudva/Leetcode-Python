class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Initialize a defaultdict to keep track of element frequencies.
        # defaultdict will automatically initialize counts to 0 for new elements.
        ctr = defaultdict(int)

        # Iterate through the list of numbers
        for n in nums:
            # Increment the count of the current element 'n'
            ctr[n] += 1

            # If there are exactly 3 unique elements in the dictionary, we need to neutralize them
            if len(ctr) == 3:
                # Create a list of keys (elements) to safely modify the dictionary while iterating
                for key in list(ctr.keys()):
                    # Decrement the count of each element by 1
                    ctr[key] -= 1
                    # If an element's count reaches 0, remove it from the dictionary
                    if ctr[key] == 0:
                        del ctr[key]

        # Now, 'ctr' contains at most 2 candidates for majority element(s).
        # Verify which of these candidates appear more than len(nums) // 3 times in the original list.
        return [n for n in ctr if nums.count(n) > len(nums) // 3]