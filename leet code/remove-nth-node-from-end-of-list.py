# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    single_jump = double_jump = head
    for i in range(n):
      double_jump = double_jump.next
    if not double_jump:
      return single_jump.next

    while double_jump.next:
      double_jump = double_jump.next
      single_jump = single_jump.next
    single_jump.next = single_jump.next.next
    return head




