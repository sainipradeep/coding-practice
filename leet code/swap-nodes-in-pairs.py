# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def swapPairs(self, head: ListNode) -> ListNode:
    temp = head
    while temp is not None:
      t = temp.val
      if temp.next is not None:
        temp.val = temp.next.val
        temp.next.val = t
        temp = temp.next.next
      else:
        temp = None
    return head
