from typing import Union

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> Union(TreeNode, None):
        t = Solution()
        if not root:
            return None
        else:
            t.invertTree(root.right)
            t.invertTree(root.left)
            root.left, root.right = root.right, root.left
            return root
