# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if p and q is None or p is None and q:
      return 0
    if p is None and q is None:
      return 1


    left = self.isSameTree(p.left, q.left)
    right = self.isSameTree(p.right, q.right)
    if not left or not right:
      return 0
    return p.val == right.val

