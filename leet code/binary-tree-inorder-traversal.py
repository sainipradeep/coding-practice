# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    stack = []
    output = []
    current = root

    while len(stack) or current:
      if current:
        stack.append(current)
        current = current.left
      else:
        node = stack.pop()
        output.append(node.val)
        if node.right is not None:
          stack.append(node.right)
          current = node.right
    return output
