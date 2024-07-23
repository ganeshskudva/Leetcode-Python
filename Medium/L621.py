class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return -1
        hp = [-f for f in collections.Counter(tasks).values()]
        heapq.heapify(hp)

        cnt = 0
        while hp:
            interval, lst = n + 1, []
            while interval and hp:
                freq = heapq.heappop(hp)
                if freq < -1:
                    lst.append(freq + 1)
                interval -= 1
                cnt += 1
            for freq in lst:
                heapq.heappush(hp, freq)
            if hp:
                cnt += interval

        return cnt
