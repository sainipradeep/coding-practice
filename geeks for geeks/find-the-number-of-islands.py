# User function Template for python3
'''
	Your task is to return the count of number
	of islands in the given boolean grid.

	Function Arguments: a (boolean grid), n -> no of rows, m -> no of columns.
	Return Type: Integer

	Contributed By: Nagendra Jha
'''


def findIslands(a):
  islands_count = 0
  for row in range(len(a)):
    for col in range(len(a[0])):
      if a[row][col] is 1:
        islands_count+=1
        traverseALlIsland(a, row, col)
  return islands_count

def traverseALlIsland( grid, row, col):
  if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or grid[row][col] is 0:
    return

  grid[row][col] = 0

  traverseALlIsland(grid, row - 1, col)
  traverseALlIsland(grid, row + 1, col)
  traverseALlIsland(grid, row, col - 1)
  traverseALlIsland(grid, row, col + 1)
  traverseALlIsland(grid, row + 1, col + 1)
  traverseALlIsland(grid, row - 1, col - 1)
  traverseALlIsland(grid, row + 1, col - 1)
  traverseALlIsland(grid, row - 1, col + 1)


if __name__ == '__main__':
  print(findIslands([[1, 1, 1, 1],[0, 0, 1, 1],[0, 1, 0, 1],[1, 0, 0,0],[0, 0, 1, 0],[1, 1, 0, 0],[0,1,1,1]]), )
