# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def kthSmallest(self, root: TreeNode, k: int) -> int:
    stack = []
    current = root
    count = 0
    while len(stack) or current:
      if current:
        stack.append(current)
        current = current.left
      else:
        node = stack.pop()
        count += 1
        if count == k:
          return node.val
        current = node.right
    return -1


if __name__ == '__main__':
    a = Solution()
    a.kthSmallest({}, 1)
