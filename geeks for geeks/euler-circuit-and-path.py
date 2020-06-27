





# User function Template for python3

def isEulerian(g, nv, ne):


  '''
  g:  dict of adjancey list, defaultdict(<class 'list'>)
      eg-: {0: [1, 2, 3], 1: [0, 2], 2: [0, 1], 3: [0, 4], 4: [3]}

  nv: num of vertices
  ne: num of edges
  return: 0/1/2
  '''



# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
from collections import defaultdict


class Graph():
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.V = vertices

  def addEdge(self, u, v):  # add directed edge from u to v.
    self.graph[u].append(v)


if __name__ == '__main__':
  test_cases = int(input())
  for cases in range(test_cases):
    N, E = map(int, input().strip().split())
    g = Graph(N)
    edges = list(map(int, input().strip().split()))

    for i in range(0, len(edges), 2):
      u, v = edges[i], edges[i + 1]
      g.addEdge(u, v)  # add an undirected edge from u to v
      g.addEdge(v, u)
    print(isEulerian(g.graph, N, E))
# } Driver Code Ends
