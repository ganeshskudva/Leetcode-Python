from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word
        freq = Counter(words)
        
        # Create a heap with (-frequency, word) tuples
        # We use negative frequency for max-heap simulation and lexicographical order as a secondary criterion
        heap = [(-count, word) for word, count in freq.items()]
        
        # Convert the list into a heap
        heapq.heapify(heap)
        
        # Extract the top k elements from the heap
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        
        return result

# Time Complexity (TC):
# 1. Counting word frequencies using Counter: O(n), where 'n' is the total number of words in the input list.
# 2. Creating the heap (list comprehension): O(m), where 'm' is the number of unique words.
# 3. Heapify operation to convert the list into a heap: O(m), since heapify is a linear-time operation.
# 4. Extracting the top k elements using heappop:
#    - Each heappop operation takes O(log m), and we perform it k times, making this step O(k * log m).
# Overall Time Complexity: O(n + m + k * log m).
# In typical scenarios, 'm' (unique words) is much smaller than 'n' (total words), making this efficient.

# Space Complexity (SC):
# 1. Storage for the frequency dictionary: O(m), where 'm' is the number of unique words.
# 2. Storage for the heap: O(m), since we store all unique words in the heap.
# 3. Storage for the result list: O(k), since we store the top k words.
# Overall Space Complexity: O(m + k).

