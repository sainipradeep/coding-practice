def nextHappyNumber(n):
  while 1:
    n += 1
    if isHappyNumber(n):
      return n

def isHappyNumber(n):
  if n is 0:
    return 0
  if n is 1 or n is 7:
    return 1
  if n<9:
    return 0

  l = list(map(int, str(n)))

  nextNumber = 0
  for i in l:
    nextNumber+=i*i
  return isHappyNumber(nextNumber)
  # return false
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      n = int(input())
      print(nextHappyNumber(n))
