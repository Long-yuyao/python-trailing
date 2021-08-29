# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or p == root or q == root:
            return root
        else:
            rr = self.lowestCommonAncestor(root.right, p, q)
            lr = self.lowestCommonAncestor(root.left, p, q)
            if not rr: return lr
            if not lr: return rr
            return root
