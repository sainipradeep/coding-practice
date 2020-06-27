def rotateArray(arr, n, k):
  g_c_d = gcd(k, n)
  for i in range(g_c_d):
    j = i
    temp = arr[i]
    d = 0
    while 1:
      d = j+k
      if d >= n:
        d = d-n
      if d == i:
        break
      arr[j] = arr[d]
      j = d
    arr[j] = temp

  print(arr)

def gcd(a, b):
  if b is 0:
    return a
  return gcd(b, a%b)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      second_line = list(map(int, input().strip().split()))
      arr = list(map(int, input().strip().split()))
      rotateArray(arr, second_line[0], second_line[1])
