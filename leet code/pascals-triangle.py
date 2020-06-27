class Solution:
  def generate(self, numRows: int):
    arr = []
    if numRows<=0:
      return arr

    for i in range(1, numRows+1):
      arr.append([0]*i)

    arr[0][0] = 1

    for i in range(1, numRows):
      for j in arr[i]:
        arr[i][j] =getValue(arr, i, j) + getValue(arr, i, j)
    return arr

def getValue(arr, row, col):
  if not isSafe(arr, row, col):
    return 0
  return arr[row][col]

def isSafe(arr, row, col):


if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
