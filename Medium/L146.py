class Node:
    def __init__(self, key=0, val=0):
        self.prev, self.next = None, None
        self.key, self.val = key, val


class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.dict, self.cap = {}, capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._insert(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])

        if len(self.dict) == self.cap:
            self._remove(self.tail.prev)

        self._insert(Node(key, value))

    def _remove(self, node):
        del self.dict[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node):
        self.dict[node.key] = node
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        nxt.prev = node
        node.next = nxt
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
