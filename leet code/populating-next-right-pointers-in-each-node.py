"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
          return root
        stack = [root]
        while len(stack):
          prev = None
          for i in range(len(stack)):
            node = stack.pop(0)
            if prev is None:

              prev = node
              node.next = None
              print("****", prev.val)
            else:
              print("----", prev.val)
              prev.next = node
              prev = node
              node.next = None
            if node.left is not None:
              stack.append(node.left)
            if node.right is not None:
              stack.append(node.right)
        return root
