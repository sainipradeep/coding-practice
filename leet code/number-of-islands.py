class Solution:
  def numIslands(self, grid) -> int:
  # def numIslands(self, grid: List[List[str]]) -> int:
    islands_count = 0
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] is '1':
          islands_count+=1
          self.traverseALlIsland(grid, row, col)
    return islands_count
  def traverseALlIsland(self, grid, row, col):
    if row <0 or row > len(grid)-1 or col < 0 or col > len(grid[0])-1 or grid[row][col] is '0':
      return

    grid[row][col] = '0'

    self.traverseALlIsland(grid, row - 1, col)
    self.traverseALlIsland(grid, row + 1, col)
    self.traverseALlIsland(grid, row, col - 1)
    self.traverseALlIsland(grid, row, col + 1)


if __name__ == '__main__':
    obj = Solution()
    print(obj.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print(obj.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
