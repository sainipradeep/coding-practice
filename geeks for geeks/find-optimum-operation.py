def findOperation(n):
  count = 0
  while n:
    if n % 2 == 0:
      n /= 2
      count += 1
    else:
      n -= 1
      count += 1
  return count

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      n = int(input())
      print(findOperation(n))
