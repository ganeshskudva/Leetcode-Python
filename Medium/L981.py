class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        arr = self.dict[key]
        low, mid, hi = 0, 0, len(arr) - 1

        while low <= hi:
            mid = (low + hi) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                low = mid + 1
            else:
                hi = mid - 1

        return "" if arr[hi][0] > timestamp else arr[hi][1]
