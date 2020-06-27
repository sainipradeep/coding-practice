class Solution:
  def findDiagonalOrder(self, nums):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    res = []
    for r, row in enumerate(nums):
      for c, col in enumerate(row):
        if len(res)<= r+c:
          res.append([])
        res[r+c].append(col)

    return [num for row in res for num in reversed(row)]

    # out = []
  #   output = []
  #   map = {}
  #   j = 0
  #   for i in range(len(nums)):
  #     output.append(nums[i][j])
  #     x = i-1
  #     y = j+1
  #     while x >= 0:
  #       if self.isSafe(x, y, nums, map):
  #         output.append(nums[x][y])
  #       x -= 1
  #       y += 1
  #
  #
  #   j = 1
  #   for i in range(0, len(nums)+ 1):
  #     if self.isSafe(j, i, nums, map):
  #       continue
  #   # x = 1
  #   # for j in range(0, len(nums)):
  #   #   if self.isSafe(x, j, nums, map):
  #   #     output.append(nums[x][j])
  #   #     x = i - 1
  #   #     y = j + 1
  #   #     while x >= 0:
  #   #       if self.isSafe(x, y, nums, map):
  #   #         output.append(nums[x][y])
  #   #         x -= 1
  #   #         y += 1
  #   #       else:
  #   #         x -= 1
  #   #         y += 1
  #   #   else:
  #   #     x -= 1
  #   return output
  #
  # def isSafe(self, i, j, nums, map):
  #   if (i<0 or j <0 or i>= len(nums) or j>= len(nums[i])) and not str(i)+str(j) in map:
  #     map[str(i) + str(j)] = 1
  #     return 0
  #   return 1
if __name__ == '__main__':
    a = Solution()
    print(a.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
    # print(a.findDiagonalOrder([[1,2]]))
