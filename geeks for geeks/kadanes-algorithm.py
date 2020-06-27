import sys
def maxSubArr(arr, n):
  max_num = arr[0]
  temp_max = max_num
  for i in range(1, n):
    temp_max = max(arr[i], arr[i]+temp_max)
    max_num = max(temp_max, max_num)
  return max_num
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      n = int(input())
      arr = list(map(int, input().strip().split()))
      print(maxSubArr(arr, n))
