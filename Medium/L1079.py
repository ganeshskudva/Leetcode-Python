class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = collections.Counter(tiles)

        def get_key(idx):
            return chr(idx + ord('A'))

        def solve():
            tot = 0
            for i in range(26):
                if not cnt[get_key(i)]:
                    continue
                tot += 1
                cnt[get_key(i)] -= 1
                tot += solve()
                cnt[get_key(i)] += 1
            return tot

        return solve()
