class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set for O(1) lookups
        num_set = set(nums)
        longest = 0  # To keep track of the longest consecutive sequence

        # Iterate through each number in the original list
        for n in nums:
            # Only start a sequence if 'n-1' is not in the set, which means 'n' is the start of a sequence
            if n - 1 not in num_set:
                length = 1  # Initialize the length of the sequence

                # Keep checking if the next consecutive number exists in the set
                while n + length in num_set:
                    length += 1
                
                # Update the longest sequence length if this one is longer
                longest = max(longest, length)
        
        # Return the length of the longest consecutive sequence
        return longest

# Time Complexity (TC):
# - Creating the set from the list takes O(n), where 'n' is the number of elements in 'nums'.
# - The outer loop runs O(n) times, and for each number, the inner loop runs at most once per element in the set.
# - Therefore, the overall time complexity is O(n) since each element is processed at most twice (once in the outer loop and once in the inner loop when it's the start of a sequence).

# Space Complexity (SC):
# - The space complexity is O(n) because we are storing the entire list of numbers in a set 'num_set'.
# - Other variables (such as 'longest' and 'length') use constant space, so the overall space complexity is O(n).