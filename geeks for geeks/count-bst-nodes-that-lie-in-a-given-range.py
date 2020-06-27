# User function Template for python3

##Structure of node
'''
# Node Class:
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None
'''


##Complete this function
def getCountOfNode(root, l, h):

  return getCount(root, l , h, 0)


def getCount(root, l , h, count):
  if root is None:
    return

  if root.left is not None and root.left
##Your code here


# {
#  Driver Code Starts
# Initial Template for Python 3

# Node Class:
class Node:
  def __init__(self):
    self.data = 0
    self.left = None
    self.right = None


def createNewNode(value):
  temp = Node()
  temp.data = value
  temp.left = None
  temp.right = None
  return temp


def newNode(root, data):
  if (root is None):
    root = createNewNode(data)
  elif (data < root.data):
    root.left = newNode(root.left, data);
  else:
    root.right = newNode(root.right, data)

  return root


def main():
  testcases = int(input())
  while (testcases > 0):
    root = None
    sizeOfArray = int(input())
    arr = [int(x) for x in input().strip().split()]
    for i in arr:
      root = newNode(root, i)

    lr = [int(x) for x in input().strip().split()]

    print(getCountOfNode(root, lr[0], lr[1]))
    testcases -= 1


if __name__ == "__main__":
  main()
# } Driver Code Ends
