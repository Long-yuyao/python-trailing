# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maxsum = -10000

    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            self.nodesum(root)
        return self.maxsum

    def nodesum(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            rsum = self.nodesum(root.right)
            lsum = self.nodesum(root.left)
            self.maxsum = max(self.maxsum, rsum+lsum+root.val)
            return max(0, rsum+root.val, lsum+root.val)


a = TreeNode(-10)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e

print(Solution().maxPathSum(a))
