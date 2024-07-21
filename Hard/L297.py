# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def solve(node):
            if node:
                vals.append(str(node.val))
                solve(node.left)
                solve(node.right)
            else:
                vals.append('#')
        vals = []
        solve(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def solve():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = solve()
            node.right = solve()
            return node
        vals = iter(data.split())
        return solve()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
