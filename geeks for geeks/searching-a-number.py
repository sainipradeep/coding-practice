def linearSearch(arr, num):
  for i, num in enumerate(numbers):
    if num == arr[1]:
      return i
  return -1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      arr = list(map(int, input().strip().split()))
      numbers = list(map(int, input().strip().split()))
      print(linearSearch(numbers, arr[1]))

