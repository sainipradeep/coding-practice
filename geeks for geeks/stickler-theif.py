def maxAmount(arr, n)->int:
  incl = 0
  excl = 0
  for i in arr:
    new_excl = max(incl+i, incl)
    incl = excl
    excl = new_excl
  return max(incl, excl)

#5 5 10 100 10 5
#0 5


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
      n = int(input())
      arr = list(map(int, input().strip().split()))
      print(maxAmount(arr, n))
