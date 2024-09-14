class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word using collections.Counter
        # Create a list of tuples where the first element is the negative frequency
        # and the second element is the word itself. 
        # We use negative frequencies to turn the default min-heap into a max-heap.
        hp = [(-v, word) for word, v in collections.Counter(words).items()]
        
        # Convert the list into a heap (min-heap by default in Python, hence negative frequency is used)
        # heapq.heapify(hp) organizes the list so that the smallest element (which is the most frequent word
        # due to the negative frequency) is at the root of the heap.
        heapq.heapify(hp)

        res = []
        # Extract the top 'k' elements from the heap
        # heappop removes and returns the smallest element from the heap (which corresponds to the word
        # with the highest frequency due to the negative frequency we used).
        # After popping each word, decrease k by 1 until we get the top 'k' frequent words.
        while hp and k:
            res.append(heapq.heappop(hp)[1])  # Append the word (which is the second element in the tuple)
            k -= 1

        # Return the result list containing the top 'k' frequent words.
        return res
