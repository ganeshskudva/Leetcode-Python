class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: the first term is "1"
        if n == 1:
            return "1"
        
        # Get the previous sequence recursively
        previous_sequence = self.countAndSay(n - 1)
        
        # Initialize an empty string for the current sequence
        current_sequence = ""
        
        # Iterate over the previous sequence and build the current sequence
        count = 1
        for i in range(1, len(previous_sequence)):
            if previous_sequence[i] == previous_sequence[i - 1]:
                count += 1
            else:
                current_sequence += str(count) + previous_sequence[i - 1]
                count = 1
        # Add the last group of characters
        current_sequence += str(count) + previous_sequence[-1]
        
        return current_sequence