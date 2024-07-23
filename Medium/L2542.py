class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, hp, res, tot = len(nums1), [], 0, 0
        ess = [[-nums2[i], nums1[i]] for i in range(len(nums1))]
        ess.sort()

        for n2, n1 in ess:
            heapq.heappush(hp, n1)
            tot += n1
            if len(hp) > k:
                tot -= heapq.heappop(hp)
            if len(hp) == k:
                res = max(res, tot * -n2)

        return res
