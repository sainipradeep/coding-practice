# User function Template for python3

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''


def compute(head):
  if head.next is None:
    return head

  result = compute(head.next)

  if result.data > head.data:
    head.data = result.data
    head.next = result.next
  else:
    head.next = result

  return head


# {
#  Driver Code Starts
# Initial Template for Python 3


# Node Class
class Node:
  def __init__(self, data):  # data -> value stored in node
    self.data = data
    self.next = None


# Linked List Class
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  # creates a new node with given value and appends it at the end of the linked list
  def append(self, new_value):
    new_node = Node(new_value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
      return
    self.tail.next = new_node
    self.tail = new_node

  def getNode(self, value):  # return node with given value, if not present return None
    curr_node = self.head
    while (curr_node.next and curr_node.data != value):
      curr_node = curr_node.next
    if (curr_node.data == value):
      return curr_node
    else:
      return None

  # prints the elements of linked list starting with head
  def printList(self):
    if self.head is None:
      print(' ')
      return
    curr_node = self.head
    while curr_node:
      print(curr_node.data, end=" ")
      curr_node = curr_node.next
    print(' ')


if __name__ == "__main__":
  t = int(input())
  while (t > 0):
    n = int(input())
    a = LinkedList()  # create a new linked list 'a'.
    nodes = list(map(int, input().strip().split()))
    for x in nodes:
      a.append(x)

    result = compute(a.head)
    a.head = result
    a.printList()
    t -= 1

# } Driver Code Ends
