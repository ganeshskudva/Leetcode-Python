class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = defaultdict(int)

        def solve(idx, width, height):
            if idx >= len(books):
                return height
            if (idx, width) in dp:
                return dp[(idx, width)]

            dp[(idx, width)] = min(
                height + solve(idx + 1, books[idx][0], books[idx][1]),
                float('inf') if width + books[idx][0] > shelfWidth else solve(idx + 1, width + books[idx][0], max(height, books[idx][1]))
            )
            return dp[(idx, width)]
        return solve(0, 0, 0)
