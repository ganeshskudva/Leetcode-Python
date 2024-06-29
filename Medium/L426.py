class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        def connect(n1, n2):
            if not n1:
                return n2
            if not n2:
                return n1

            tail1, tail2 = n1.left, n2.left
            tail1.right = n2
            n2.left = tail1
            tail2.right = n1
            n1.left = tail2

            return n1

        left_head, right_head = self.treeToDoublyList(root.left), self.treeToDoublyList(root.right)
        root.left = root.right = root

        return connect(connect(left_head, root), right_head)
