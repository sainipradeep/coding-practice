# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def pruneTree(self, root: TreeNode) -> TreeNode:
    if root is None:
      return None
    root.left = self.pruneTree(root.left)
    root.right = self.pruneTree(root.right)

    if not root.left or not root.right or root.val is 0:
     return None
    return root

