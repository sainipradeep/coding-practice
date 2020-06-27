# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSymmetric(self, root: TreeNode) -> bool:
    return self.isMirrortree(root.left, root.right)
  def isMirrortree(self, root1, root2):
    if root1 is None and root2 is None:
      return 1
    if (root1 and root2 is None) or (root1 is None and root2):
      return 0
    left = self.isMirrortree(root1.left, root2.right)
    right = self.isMirrortree(root1.right, root2.left)

    if not left or not right  or root1.val != root2.val:
      return 0
    return 1

    # if (root1.left and root2.right is None) or (root1.right and root.r):
    #   return 0

