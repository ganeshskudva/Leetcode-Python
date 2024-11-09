from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Calculate the maximum number of candies once
        max_candies = max(candies)  # O(n) time complexity
        
        # Return a list where each element is True if the child can have the maximum or more candies with extraCandies
        return [n + extraCandies >= max_candies for n in candies]  # O(n) time complexity for list comprehension

# Time Complexity (TC): O(n)
# - Calculating max(candies) takes O(n).
# - The list comprehension also takes O(n) as it iterates through the candies list once.
# - Therefore, the total time complexity is O(n) + O(n) = O(n).

# Space Complexity (SC): O(n)
# - We require O(n) additional space for the output list, where n is the number of elements in the candies list.
# - No additional space is used other than the output list, so the overall space complexity is O(n
