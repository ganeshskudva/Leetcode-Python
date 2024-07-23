class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s

        max_heap = [(-freq, char) for char, freq in collections.Counter(s).items()]
        heapq.heapify(max_heap)

        wait_queue = deque()
        result = []

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            wait_queue.append((freq + 1, char))  # Decrement frequency and add to wait queue

            if len(wait_queue) >= k:
                freq, char = wait_queue.popleft()
                if freq < 0:
                    heapq.heappush(max_heap, (freq, char))

        rearranged = "".join(result)
        return rearranged if len(rearranged) == len(s) else ""
