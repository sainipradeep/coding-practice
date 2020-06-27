# your task is to complete this function
# function should return new head pointer
'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''


def deleteAllOccurances(head, k):
  # Code here
  if head is None:
    return
  prev = head
  temp = head



# {
#  Driver Code Starts
# Node Class
class node:
  def __init__(self):
    self.data = None
    self.next = None


# Linked List Class
class Linked_List:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert(self, data):
    if self.head == None:
      self.head = node()
      self.tail = self.head
      self.head.data = data
    else:
      new_node = node()
      new_node.data = data
      new_node.next = None
      self.tail.next = new_node
      self.tail = self.tail.next


def printlist(head):
  temp = head
  while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next
  print('')


# Driver Program
if __name__ == '__main__':
  t = int(input())
  for i in range(t):
    list1 = Linked_List()
    n = int(input())
    values = list(map(int, input().strip().split()))
    for i in values:
      list1.insert(i)
    k = int(input())
    newhead = deleteAllOccurances(list1.head, k)
    printlist(newhead)
# Contributed By: Harshit Sidhwa
# } Driver Code Ends
