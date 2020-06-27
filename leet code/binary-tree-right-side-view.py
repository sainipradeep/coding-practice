# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def rightSideView(self, root: TreeNode) -> List[int]:
    list = []
    if root is None:
      return list
    self.getRightSideView(root, {}, list, 0)
    return list

  def getRightSideView(self, root, map, list, count):
    if root is None:
      return
    if not count in map:
      list.append(root.val)
      map[count] = 1
    self.getRightSideView(root.right, map, list, count + 1)
    self.getRightSideView(root.left, map, list, count + 1)
