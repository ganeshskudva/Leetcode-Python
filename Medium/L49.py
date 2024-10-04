class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict with lists as default values to store anagram groups
        map = defaultdict(list)
        
        # Iterate through each word in the input list of strings
        for word in strs:
            # Create a frequency count tuple for each word (26 zeros for each letter a-z)
            count = [0] * 26
            for char in word:
                # Increment the corresponding position in the count for each character
                count[ord(char) - ord('a')] += 1
            
            # Use the tuple of counts as a key to group anagrams
            map[tuple(count)].append(word)
        
        # Return all the values (lists of anagrams) from the map as the final result
        return list(map.values())
