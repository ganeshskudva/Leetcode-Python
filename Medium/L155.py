class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = LLNode(val, val, None)
        else:
            self.head = LLNode(val, min(self.head.min, val), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min


class LLNode:
    def __init__(self, val, mini, next):
        self.val = val
        self.min = mini
        self.next = next
