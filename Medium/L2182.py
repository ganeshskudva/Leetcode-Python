from heapq import heapify, heappop, heappush
from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Step 1: Create a max heap based on character ASCII values and frequencies
        # Ordinals (negated for max-heap simulation), frequencies stored in the heap
        pq = [(-ord(k), v) for k, v in Counter(s).items()]  
        heapify(pq)  # Heapify the list to form a max-heap
        # Time Complexity: O(m), where m is the number of unique characters in s
        # Space Complexity: O(m), for storing the heap elements

        ans = []  # Result list to store characters in order
        # Space Complexity: O(n), where n is the length of the string s

        while pq: 
            k, v = heappop(pq)  # Pop the character with the largest ASCII value
            if ans and ans[-1] == k:  # If the previous character is the same, avoid consecutive duplicates
                if not pq:  # If no other character is available, stop processing
                    break 
                # Pop the second largest character
                kk, vv = heappop(pq)  
                ans.append(kk)  # Append this character once
                if vv-1:  # If more occurrences are left, push it back into the heap
                    heappush(pq, (kk, vv-1))
                heappush(pq, (k, v))  # Push the original character back into the heap
            else: 
                # Use the current character up to 'repeatLimit' times
                m = min(v, repeatLimit)
                ans.extend([k] * m)
                # If there are remaining occurrences, reinsert it into the heap
                if v - m: 
                    heappush(pq, (k, v - m))

        # Convert ASCII values back to characters and join to form the result string
        return "".join(chr(-x) for x in ans)
        
# Time Complexity: O(n log m), where:
#   n = length of the string (total operations for each character)
#   m = number of unique characters (heap size for push/pop operations)
# Space Complexity: O(n + m), where n is for the result string and m for the heap
