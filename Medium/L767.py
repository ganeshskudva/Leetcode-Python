import heapq
import collections

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count the frequency of each character in the string 's'
        freq_map = collections.Counter(s)  # Example: {'a': 3, 'b': 2, 'c': 1}
        # Time Complexity: O(n), where n is the length of the string s
        
        # Step 2: Create a max heap based on frequencies by using negative frequencies
        max_heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(max_heap)  # Turn list into a max-heap (using negative values)
        # Time Complexity for heapify: O(m), where m is the number of unique characters in s
        # Space Complexity: O(m) for storing the heap elements

        # Step 3: Check if it is possible to rearrange the string
        # If any character's frequency is greater than (len(s) + 1) // 2, return ""
        if -max_heap[0][0] > (len(s) + 1) // 2:
            return ""
        # Explanation: If the highest frequency is more than half the string length, 
        # it is impossible to rearrange the string to avoid adjacent duplicates.
        
        res = []  # This will store the reorganized result string
        # Space Complexity: O(n) for the result, as it stores each character of s
        
        prev_freq, prev_char = 0, ''  # Track the previous character and its frequency

        # Step 4: Process the heap by placing characters alternately
        while max_heap:
            # Pop character with the highest frequency from heap
            freq, char = heapq.heappop(max_heap)
            res.append(char)  # Append character to the result
            
            # Step 5: Add the previous character back to the heap if its frequency is still positive
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            # Update previous character and its frequency (decrease frequency by 1)
            prev_freq, prev_char = freq + 1, char  # Increment because freq is negative
            
            # Time Complexity for each heappop and heappush: O(log m)
            # Since we perform heappop/heappush for each character, overall time for heap operations is O(n log m)

        return ''.join(res)  # Join the list into a final string
        # Time Complexity for join: O(n)

# Overall Time Complexity: O(n log m), where n is the length of s and m is the number of unique characters
#   - Counting character frequencies: O(n)
#   - Building the max heap: O(m)
#   - Processing each character with heappop/heappush operations: O(n log m)

# Overall Space Complexity: O(n)
#   - O(m) for the heap and frequency map
#   - O(n) for the result list storing each character of the reorganized string
