class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count the frequency of each character in the string 's'
        freq_map = collections.Counter(s)  # Example: {'a': 3, 'b': 2, 'c': 1}

        # Step 2: Create a max heap based on frequencies (-freq for max-heap)
        max_heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(max_heap)  # Turns the list into a heap in O(m) time (where m is the number of unique characters)

        # Step 3: Check if it is possible to rearrange the string
        if -max_heap[0][0] > (len(s) + 1) // 2:
            return ""

        res = []  # This will store the result

        # Step 4: Process the heap by placing characters alternatively
        prev_freq, prev_char = 0, ''

        while max_heap:
            freq, char = heapq.heappop(max_heap)  # Get the character with the highest frequency
            res.append(char)  # Place the character in the result

            # Step 5: Add the previous character back to the heap if its frequency is still greater than zero
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            # Update the previous character and its frequency (decrease frequency by 1)
            prev_freq, prev_char = freq + 1, char  # freq is negative, so incrementing brings it closer to zero

        return ''.join(res)