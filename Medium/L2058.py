class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res, prev, curr = [], head, head.next
        pos = 1

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                res.append(pos)
                prev, curr = curr, curr.next
                pos += 1

        if len(res) < 2:
            return [-1, -1]

        min_dist, max_dist = float('inf'),res[-1] - res[0]
        for i in range(1, len(res)):
            min_dist = min(min_dist, res[i] - res[i - 1])
        
        return [min_dist, max_dist]
