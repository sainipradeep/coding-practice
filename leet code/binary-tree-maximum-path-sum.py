# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  maxSum = float('-inf')
  def maxPathSum(self, root: TreeNode) -> int:
    self.findMaxSum(root)
    return self.maxSum

  def findMaxSum(self, root):
    if root is None:
      return 0

    left = max(0, self.findMaxSum(root.left))
    right = max(0, self.findMaxSum(root.right))

    self.maxSum = max(self.maxSum, root.val+ left+ right)
    return root.val + max(left, right)
