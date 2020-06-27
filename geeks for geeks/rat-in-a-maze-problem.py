#User function Template for python3


def findPath(arr, n):
  visited_path = [[0 for i in range(n)] for i in range(n)]
  outputPaths =[]
  nextStep(arr, n, 0, 0, visited_path, "", outputPaths)

  output = ""
  for i in outputPaths:
    output += i+ " "
  return output


def canMove(arr, n, row, col, visited_path):
  if row is -1 or row is n or col is -1 or col is n or visited_path[row][col] is 1 or arr[row][col] is 0 :
    return 0
  return 1

def nextStep(arr, n, row, col, visited_path, path, outputPaths):
  if not canMove(arr, n, row, col, visited_path):
    return

  if row is n-1 and col is n-1:
    outputPaths.append(path)
    return

  visited_path[row][col] = 1

  if canMove(arr, n, row+1, col, visited_path):
    path += "D"
    nextStep(arr, n, row+1, col, visited_path, path, outputPaths)
    path = path[:-1]

  if canMove(arr, n, row, col - 1, visited_path):
    path += "L"
    nextStep(arr, n, row, col - 1, visited_path, path, outputPaths)
    path = path[:-1]
  if canMove(arr, n, row, col + 1, visited_path):
    path += "R"
    nextStep(arr, n, row, col + 1, visited_path, path, outputPaths)
    path = path[:-1]

  if canMove(arr, n, row-1, col, visited_path):
    path +="U"
    nextStep(arr, n, row-1, col, visited_path, path, outputPaths)
    path = path[:-1]

  visited_path[row][col] = 0




#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k = 0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k += 1

        result = findPath(matrix, n[0])
        if result == "" :
            print(-1)
        else:
            print(result)
# } Driver Code Ends
