def searchInList(numbers, k, l, r):
  while l <= r:
    mid = (l + (r - 1)) // 2

    if numbers[mid] == k:
      return 1
    elif numbers[mid] < k:
      l = mid + 1
    else:
      r = mid - 1
  return -1


if __name__ == '__main__':
  t = int(input())
  for _ in range(t):
    arr = list(map(int, input().strip().split()))
    numbers = list(map(int, input().strip().split()))
    print(searchInList(numbers, arr[1], 0, len(numbers)))
