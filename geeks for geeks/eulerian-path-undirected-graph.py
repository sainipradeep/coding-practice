def is_euler_graph(graph):
  graphVerticesSum = list()

  for i in range(n):
    graphVerticesSum.append(sum(graph[i]))
  oddVertices = 0
  for i in range(n - 1, -1, -1):
    if graphVerticesSum[i] % 2 is 1:
      oddVertices += 1

  if oddVertices > 2:
    return 0

  return 1




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      n = int(input())
      graph = [[0 for i in range(n)] for i in range(n)]
      for i in range(n):
        vertices = list(map(int, input().strip().split()))
        for j in range(n):
          graph[i][j] = vertices[j]

      print(is_euler_graph(graph))
