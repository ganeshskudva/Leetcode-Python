class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        union = [i for i in range(n)]

        def find(node):
            if union[node] == node:
                return node

            union[node] = find(union[node])
            return union[node]

        for a, b in allowedSwaps:
            parent_a, parent_b = find(a), find(b)
            if parent_a != parent_b:
                union[parent_a] = parent_b

        mp = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            num, root = target[i], find(i)
            mp[root][num] += 1

        res = 0
        for i in range(n):
            num, root = source[i], find(i)
            if not mp[root][num]:
                res += 1
            else:
                mp[root][num] -= 1

        return res
