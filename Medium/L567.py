class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # Frequency count of characters in s1
        freq_s1 = collections.Counter(s1)
        
        # Frequency count for the sliding window in s2
        freq_s2 = defaultdict(int)
        
        # Count of how many characters in freq_s2 match with freq_s1
        matches = 0
        # Number of unique characters in s1
        required_matches = len(freq_s1)
        
        # Initialize the sliding window
        start = 0
        
        for end in range(len(s2)):
            # Add the current character from s2 to the sliding window (increment its frequency)
            char = s2[end]
            freq_s2[char] += 1

            # If the character's frequency matches in both s1 and the current window, update matches count
            if char in freq_s1 and freq_s2[char] == freq_s1[char]:
                matches += 1

            # If the window size exceeds the size of s1, shrink the window from the left
            if end >= len(s1):
                left_char = s2[start]
                if left_char in freq_s1 and freq_s2[left_char] == freq_s1[left_char]:
                    matches -= 1  # Decrement matches if the left character is causing a match
                
                # Decrease the frequency of the left character as we slide the window
                freq_s2[left_char] -= 1
                start += 1

            # If the number of matches equals the number of unique characters in s1, we found a permutation
            if matches == required_matches:
                return True

        # If no valid permutation is found, return False
        return False

        