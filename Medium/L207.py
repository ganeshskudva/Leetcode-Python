class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg, q, vis = [0] * numCourses, deque(), set()
        lst = defaultdict(list)

        for p in prerequisites:
            indeg[p[0]] += 1
            lst[p[1]].append(p[0])
        for i in range(len(indeg)):
            if not indeg[i]:
                q.append(i)

        while q:
            size = len(q)
            for _ in range(size):
                n = q.popleft()
                if n in vis:
                    continue
                vis.add(n)
                for c in lst[n]:
                    indeg[c] -= 1
                    if not indeg[c]:
                        q.append(c)

        return numCourses == len(vis)
