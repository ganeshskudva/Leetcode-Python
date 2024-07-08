class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = [i for i in range(1, n + 1)]
        
        while len(q) != 1:
            x = k
            while x > 1:
                r = q.pop(0)
                q.append(r)
                x -= 1
            q.pop(0)
        
        return q[0]
