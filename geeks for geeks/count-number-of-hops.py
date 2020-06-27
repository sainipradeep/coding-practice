# def getHopsCount(n):
#   if n <=1:
#     return 1
#   elif n == 2:
#     return 2
#   return getHopsCount(n-3)+getHopsCount(n-2)+getHopsCount(n-1)

def getHopsCount(n):
  if n == 1:
    return 1
  arr = [0] * (n+1)
  arr[0] = 1
  arr[1] = 1
  arr[2] = 2

  for i in range(3, n+1):
    arr[i] = arr[i-3] +arr[i-2] +arr[i-1]
  # return getHopsCount(n-3)+getHopsCount(n-2)+getHopsCount(n-1)
  return arr[n]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
      n = int(input())
      print(getHopsCount(n))
