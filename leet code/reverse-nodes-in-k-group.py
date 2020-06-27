# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    front = None
    temp = head
    counter = 0
    start = head
    while temp is not None:
      if counter == k:
        s = self.swap(start, k)
        if front is None:
          front = s
        counter = 0
        start = a
      temp = temp.next
      counter += 1
    return front

  def swap(self, head, k):
    temp = head
    curr = head
    next = None
    prev = None

    while curr is not None and k:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
      k -= 1
    temp.next = curr
    return prev



# {
#  Driver Code Starts

# Linked List Class
class Linked_List:
  def __init__(self):
    self.head = None
    self.lastNode = None

  def insert(self, val):
    if self.head == None:
      self.head = ListNode(val)
      self.lastNode = self.head
    else:
      new_node = ListNode(val)
      self.lastNode.next = new_node
      self.lastNode = new_node

  def createList(self, arr, n):
    for i in range(n):
      self.insert(arr[i])
    return self.head

  def printList(self):
    tmp = self.head
    while tmp is not None:
      print(tmp.data, end=" ")
      tmp = tmp.next
    print()


if __name__ == '__main__':
  n = int(input())
  arr = list(map(int, input().strip().split()))
  lis = Linked_List()
  k = int(input())
  head = lis.createList(arr, n)
  obj = Solution()
  obj.reverseKGroup(head, k)
  # lis.printList()
