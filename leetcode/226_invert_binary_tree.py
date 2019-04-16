# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        t = Solution()
        if not root:
            return
        else:
            t.invertTree(root.right)
            t.invertTree(root.left)
            root.left, root.right = root.right, root.left
            return root
