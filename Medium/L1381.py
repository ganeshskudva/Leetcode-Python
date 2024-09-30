class CustomStack:

    def __init__(self, maxSize: int):
        self.st = []
        self.cap = maxSize
    def push(self, x: int) -> None:
        if len(self.st) == self.cap:
            return 
        self.st.append(x)

    def pop(self) -> int:
        if not self.st:
            return -1
        
        return self.st.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.st), k)):
            self.st[i] += val