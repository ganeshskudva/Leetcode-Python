class TimeMap:

    def __init__(self):
        # Initialize a dictionary where each key maps to a list of tuples (timestamp, value).
        # defaultdict is used to automatically initialize the value as an empty list if the key doesn't exist.
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append a tuple (timestamp, value) to the list associated with the given key.
        # This allows us to store multiple (timestamp, value) pairs for the same key.
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If the key is not in the dictionary, return an empty string as there's no data.
        if key not in self.dict:
            return ""

        # Set up binary search variables:
        # 'lo' and 'hi' are the low and high pointers for the binary search.
        # 'mid' is the midpoint.
        # 'arr' is the list of (timestamp, value) pairs for the given key.
        lo, hi, mid, arr = 0, len(self.dict[key]) - 1, 0, self.dict[key]

        # Perform binary search to find the closest timestamp <= the given 'timestamp'.
        while lo <= hi:
            mid = (lo + hi) // 2  # Calculate the midpoint.
            
            # If the exact timestamp is found, return the corresponding value.
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            
            # If the timestamp at 'mid' is greater than the target timestamp, 
            # move the search to the left half (i.e., adjust 'hi').
            if arr[mid][0] > timestamp:
                hi = mid - 1
            else:
                # Otherwise, move the search to the right half (i.e., adjust 'lo').
                lo = mid + 1

        # After the binary search, 'hi' will be the greatest index where arr[hi][0] <= timestamp.
        # If 'hi' is negative (i.e., no valid timestamp <= target), return an empty string.
        # Otherwise, return the value corresponding to the largest timestamp <= the target timestamp.
        return "" if hi < 0 else arr[hi][1]

