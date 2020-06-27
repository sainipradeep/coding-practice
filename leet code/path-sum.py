# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if root is None:
      return 0
    if root.left is None and root.right is None:
      return (root.val - sum) is 0
    return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
