def findMinWork(works):
  if len(works) is 1:
    return works[0]
  p1 = works[0]
  p2 = works[1]
  for i in range(2, n):
    temp = min(p1, p2)
    p1 = p2
    p2 += works[i]

  return min(p1, p2)




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      n = int(input())
      works = list(map(int, input().strip().split()))
      print(findMinWord(works, n))

