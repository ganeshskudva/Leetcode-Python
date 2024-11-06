class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Helper function to calculate the squared Euclidean distance from origin
        def dist(x, y):
            return x**2 + y**2  # We avoid square root to simplify calculations

        hp = []  # Max-heap to store the k closest points by negative distance for max-heap simulation
        for x, y in points:
            heappush(hp, (-dist(x, y), x, y))  # Push negative distance for max-heap behavior
            if len(hp) > k:  # If heap size exceeds k, remove the farthest point
                heappop(hp)

        # Extract and return the k closest points from the heap
        return [[x, y] for _, x, y in hp]

        # TC: O(n log k), where n is the number of points.
        #   - We iterate over each point and perform an O(log k) operation for insertion in the heap.
        #   - The heappop operation is also O(log k), which we do only when the heap exceeds size k.

        # SC: O(k), as we maintain a max-heap of size up to k to store the closest points.
