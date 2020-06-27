# def printLeader(arr, n, start_index, output):
#   if start_index is n - 1:
#     output.append(arr[start_index])
#     return output
#
#   temp_output = printLeader(arr, n, start_index + 1, output)
#   if arr[start_index] >= temp_output[len(temp_output) - 1]:
#     output.append(arr[start_index])
#
#   return output
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#       n = int(input())
#       arr = list(map(int, input().strip().split()))
#       output = []
#       printLeader(arr, n, 0, output)
#       while len(output):
#         print(output.pop(), end=" ")
#       print()

def printLeader(arr, n):
  stack = [arr[-1]]
  for i in range(n-2, 0, -1):
    if arr[i] >= stack[-1]:
      stack.append(arr[i])

  while len(stack):
    print(stack.pop(), end=" ")


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      n = int(input())
      arr = list(map(int, input().strip().split()))
      printLeader(arr, n)
      print()
