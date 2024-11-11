class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        # Result list to store the run-length encoded product
        product_encoded = []
        # Initialize pointers for both encoded arrays
        idx1 = idx2 = 0
        # Initialize frequency counters for both lists with the first element's frequency
        freq1, freq2 = encoded1[0][1], encoded2[0][1]
        
        # Loop until we exhaust one of the encoded arrays
        while idx1 < len(encoded1) and idx2 < len(encoded2):
            # Get the current values to multiply from both encoded lists
            val1 = encoded1[idx1][0]
            val2 = encoded2[idx2][0]
            
            # Calculate the product of the two values
            prod = val1 * val2
            
            # Determine the minimum frequency between the two elements
            min_freq = min(freq1, freq2)
            
            # Decrease the current frequencies by min_freq
            freq1 -= min_freq
            freq2 -= min_freq
            
            # Move to the next element in encoded1 if its frequency has been exhausted
            if freq1 == 0:
                idx1 += 1
                # Update freq1 to the next element's frequency if within bounds
                freq1 = encoded1[idx1][1] if idx1 < len(encoded1) else 0
            
            # Move to the next element in encoded2 if its frequency has been exhausted
            if freq2 == 0:
                idx2 += 1
                # Update freq2 to the next element's frequency if within bounds
                freq2 = encoded2[idx2][1] if idx2 < len(encoded2) else 0
            
            # Check if we should start a new entry or extend the last entry in `product_encoded`
            if not product_encoded or product_encoded[-1][0] != prod:
                # If this is the first product or the product differs from the last entry
                product_encoded.append([prod, min_freq])
            else:
                # If the last entry has the same product value, we combine frequencies
                product_encoded[-1][1] += min_freq
        
        # Return the final encoded product
        return product_encoded

# Time Complexity (TC): O(m + n), where m is the length of `encoded1` and n is the length of `encoded2`.
# - Each element of `encoded1` and `encoded2` is processed at most once, making the time complexity linear 
#   in relation to the sum of their lengths.

# Space Complexity (SC): O(m + n), where `m + n` represents the maximum number of distinct products in `product_encoded`.
# - In the worst case, each unique pair of elements from `encoded1` and `encoded2` could create a new entry 
#   in `product_encoded`. Although it's unlikely, we assume up to `m + n` entries could be added, so the 
#   space complexity is O(m + n) for the result storage.
