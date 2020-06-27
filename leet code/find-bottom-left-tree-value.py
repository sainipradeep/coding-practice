# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def findBottomLeftValue(self, root: TreeNode) -> int:
    if root is None:
      return root
    list = []
    self.getBottomLeftValue(root, {}, 0)
    return list[0]
  def getBottomLeftValue(self, root, map, depth,list):
    if root is None:
      return
    if not depth in map:
      map[depth] = 1
      list[0] = root.val
    self.getBottomLeftValue(root.left, map, depth+1, list)
    self.getBottomLeftValue(root.right, map, depth, list)


