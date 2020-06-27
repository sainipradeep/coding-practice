# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def minDepth(self, root: TreeNode) -> int:
    if root is None:
      return 0
    return self.getMinDepth(root, 1)
  def getMinDepth(self, root, depth)-> int:
    if root is None:
      return depth
    left = depth
    right = depth
    if root.left is not None:
      left = self.getMinDepth(root.left, depth+1)
    if root.right  is not None:
      right = self.getMinDepth(root.right, depth+1)
    return min(left, right)
