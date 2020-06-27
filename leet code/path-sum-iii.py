# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pathSum(self, root: TreeNode, sum: int) -> int:
    if root is None:
      return 0
    self.getPathSum(root, sum, 0)
  def getPathSum(self, root, sum, count)->int:
    if root is None:
      return 0

    if root.val is sum:
      return 1

    return self.getPathSum(root.left,sum, sum-root.val) + self.getPathSum(root.right, sum, sum-root.val)
