# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: TreeNode) -> list:
        tree = [[root]]
        visited = [[root.val]]
        while tree:
            stack = []
            stack_val = []
            for r in tree[0]:
                if r.left:
                    stack.append(r.left)
                    stack_val.append(r.left.val)
                if r.right:
                    stack.append(r.right)
                    stack_val.append(r.right.val)
            tree.pop(0)
            if stack:
                tree.append(stack)
                visited.append(stack_val)
        return visited


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e
print(Solution().levelOrder(a))


