# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
  def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    if root is None:
      return []
    result = deque()
    stack = [root]
    while len(stack):
      l = []
      for i in range(len(stack)):
        node = stack.pop(0)
        if node.left is not None:
          stack.append(node.left)
        if node.right is not  None:
          stack.append(node.right)
        l.append(node.val)
      result.appendleft(l)
    return result





