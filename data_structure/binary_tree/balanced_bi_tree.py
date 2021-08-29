# https://leetcode-cn.com/problems/balanced-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            dl = self.depth(root.left)
            dr = self.depth(root.right)
            if dl == -1 or dr == -1:
                return -1
            elif max(dl, dr) - min(dl, dr) >= 2:
                return -1
            else:
                return max(dl, dr) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if self.depth(root) != -1:
            return True
        else:
            return False
