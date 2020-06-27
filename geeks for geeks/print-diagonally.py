# def isSafe(arr, n , col, row):
#   if row is -1 or row is n or col is -1 or col is n:
#     return 0
#   return 1
def printDiagonal(arr, n):
  result = []
  for r, row in enumerate(arr):
    for c, num in enumerate(row):
      if len(result) <= r+c:
        result.append([])
      result[r+c].append(num)
  for row in result:
    for num in row:
      print(num, end=" ")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      n = int(input())
      arr = [[0 for i in range(n) ] for i in range(n)]
      input_arr = list(map(int, input().strip().split()))
      index =0
      for i in range(n):
        for j in range(n):
          arr[i][j] = input_arr[index]
          index+=1
      printDiagonal(arr, n)
      print()
