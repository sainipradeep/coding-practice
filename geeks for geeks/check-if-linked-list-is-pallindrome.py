# User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.

	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''


def isPalindrome(head):
  if head is None:
    return

  mid_index =0
  mid = head
  next = mid.next
  stack = [mid.data]
  while next is not None:
    mid = mid.next
    stack.append(mid.data)
    if next.next is not None:
      next = next.next.next
    else:
      next = None
    mid_index+=1

  # if mid_index % 2 == 0:
  #   stack
  flag = 1
  while mid is not None:
    if mid.data is not stack.pop():
      flag = 0
      break
    mid = mid.next
  return flag



# code here


# {
#  Driver Code Starts
# Initial Template for Python 3
# Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
  sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


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
    else:
      self.tail.next = new_node
    self.tail = new_node

  # returns the size of linked list


def getSize(head):
  count = 0
  curr_node = head
  while curr_node:
    count += 1
    curr_node = curr_node.next
  return count


if __name__ == "__main__":
  t = int(input())
  for _ in range(0, t):
    n = int(input())
    a = LinkedList()  # create a new linked list 'a'.
    nodes_a = list(map(int, input().strip().split()))
    for x in nodes_a:
      a.append(x)  # add to the end of the list

    if isPalindrome(a.head):
      print(1)
    else:
      print(0)

# } Driver Code Ends
