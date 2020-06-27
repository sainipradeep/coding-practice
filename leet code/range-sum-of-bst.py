# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    if root is None:
      return 0



    left = self.rangeSumBST(root.left, L, R)
    right = self.rangeSumBST(root.right, L, R)

    if root.val > L and root.val< R:
      left+=root.val

    return left+right
