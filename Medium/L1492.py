class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        root = math.sqrt(n)
        
        for i in range(1, math.ceil(root)):
            if n%i == 0:
                k -= 1
                if k == 0:
                    return i
        
        for i in range(int(root), 0, -1):
            if n%i ==0:
                k -= 1
                if k ==0:
                    return n//i
        
        return -1
        
