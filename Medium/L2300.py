class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Initialize the result list with zeroes, one for each spell
        res = [0] * len(spells)

        # Sort the potions to apply binary search on them efficiently
        potions.sort()

        # Loop through each spell
        for i in range(len(spells)):
            low, high = 0, len(potions) - 1  # Binary search boundaries
            
            # Perform binary search to find the first potion that, when paired with the current spell, 
            # results in a product greater than or equal to the success threshold
            while low <= high:
                mid = (low + high) // 2  # Calculate the midpoint
                
                # Check if the current spell and the mid potion meet the success condition
                if (spells[i] * potions[mid]) >= success:
                    high = mid - 1  # If the product is large enough, move the high pointer to the left to find smaller valid potions
                else:
                    low = mid + 1  # If the product is too small, move the low pointer to the right to find larger potions
            
            # After binary search, 'low' will be the index of the first valid potion that meets the success condition
            # The number of successful pairs for this spell is the number of potions from 'low' to the end of the list
            res[i] = len(potions) - low

        return res
