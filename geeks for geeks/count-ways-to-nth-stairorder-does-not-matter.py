# if __name__ == '__main__':
#   t = int(input())
#   arr = [0] * (100002)
#   arr[0] = 1
#   arr[1] = 1
#   c = 1000000007
#   for j in range(2, 100002):
#     arr[j] = ((arr[j - 2]% c) +(arr[j - 1]% c)) % c
#   for i in range(t):
#     n = int(input())
#     print(arr[n])


if __name__ == '__main__':
  arr = [0] * (100002)
  arr[0] = 1
  arr[1] = 1
  arr[2] = 2
  for j in range(3, 100001):
    if j % 2 == 0:
      arr[j] = arr[j - 1] + 1
    else:
      arr[j] = arr[j - 1]
  t = int(input())
  for i in range(t):
    n = int(input())
    print(arr[n])
    print("hello")


