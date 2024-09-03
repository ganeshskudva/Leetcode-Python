class Solution:
    def getLucky(self, s, k):
        # Convert each character to its corresponding numeric value
        number = ''.join(str(ord(x) - ord('a') + 1) for x in s)
        
        # Perform the transformation `k` times
        for _ in range(k):
            number = str(sum(int(x) for x in number))
        
        return int(number)
