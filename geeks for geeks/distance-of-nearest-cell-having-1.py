import collections
def distance(matrix, m, n):
  queue = collections.deque()
  for i in range(m):
    for j in range(n):
      if matrix[i][j] is 0:
        queue.append((i, j))
      else:
        matrix[i][j] = float("inf")

  directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

  while len(queue):
    cell = queue.popleft()
    for dirC in directions:
      i, j = cell[0] + dirC[0], cell[1] + dirC[1]
      if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= matrix[cell[0]][cell[1]] + 1:
        continue
      queue.append((i, j))
      matrix[i][j] = matrix[cell[0]][cell[1]] + 1
  return matrix

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      sizes = list(map(int, input().strip().split()))
      str = list(map(int, input().strip().split()))
      matrix =[[0 for i in range(sizes[0])] for i in range(sizes[1])]
      index = 0
      for i in range(sizes[0]):
        for j in range(sizes[1]):
          matrix[i][j] = str[index]
          index += 1
      distance(matrix, sizes[0], sizes[1])
      for i in range(sizes[0]):
        for j in range(sizes[1]):
          print(matrix[i][j], end=" ")
        print()

