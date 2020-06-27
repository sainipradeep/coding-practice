class Solution:
  def maxArea(self, height) -> int:
    length = len(height)
    if length <=1:
      return 0
    output = 0
    left = 0
    right = length-1

    while left < right:
      output = max(output, (min(height[left], height[right]) * (length-1)))
      if height[left]>height[right]:
        right -= 1
      else:
        left += 1
      length-=1

    return output

if __name__ == '__main__':
  a = Solution()
  print(a.maxArea([1,8,6,2,5,4,8,3,7]))
