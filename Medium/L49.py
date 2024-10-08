class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Time complexity: O(n * k), where n is the number of strings in the input list,
        # and k is the maximum length of a string. For each string, we process k characters.
        # Space complexity: O(n * k), for storing the result in the hash map and the output list.
        
        # We will use a hashmap (defaultdict) to store lists of anagrams.
        # The key will be a tuple representing the count of each character (from 'a' to 'z') in the string.
        # The value will be the list of strings that share the same character frequency tuple.

        hmap = collections.defaultdict(list)  # Initialize a default dictionary to group anagrams.

        # Iterate through each string in the input list.
        for st in strs:
            # Create an array of size 26 (one for each lowercase letter).
            # This array will keep track of the frequency of each character in the string.
            array = [0] * 26  # O(26) = O(1) because it's a constant size.
            
            # Iterate through each character in the current string.
            for l in st:
                # Increment the position corresponding to the character in the array.
                # We use `ord(l) - ord('a')` to map each character to its respective index (0-25).
                array[ord(l) - ord('a')] += 1
            
            # Convert the array to a tuple (which is hashable) and use it as the key in the hashmap.
            # All strings that have the same character counts will be grouped together.
            hmap[tuple(array)].append(st)

        # Return the grouped anagrams by returning the values of the hashmap.
        # Each value in the hashmap is a list of anagrams.
        return hmap.values()

# Time Complexity (TC):
# - Building the frequency array for each string takes O(k), where k is the length of the string.
# - We do this for all n strings, so the overall time complexity is O(n * k).

# Space Complexity (SC):
# - The hashmap stores n keys (one for each unique tuple) and each key maps to a list of strings.
# - Each key (the tuple) has a size of 26 (fixed length), but each string takes O(k) space.
# - So, the space complexity for the hashmap is O(n * k), where n is the number of strings and k is the length of the strings.
