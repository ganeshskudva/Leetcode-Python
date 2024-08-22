class Logger:

    def __init__(self):
        self.q = deque()
        self.st = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.q and timestamp - self.q[0][0] >= 10:
            self.st.remove(self.q.popleft()[1])
        if message in self.st:
            return False
        self.q.append((timestamp, message))
        self.st.add(message)
        return True
