class Solution:
  def find132pattern(self, nums):
    
    st = float("-inf")
    stack = []
    for i in range(len(nums)-1, -1, -1):
      if nums[i] < st:
        return 1
      else:
        while len(stack) and nums[i] > stack[-1]:
          st = stack.pop()
      stack.append(nums[i])
    return 0

if __name__ == '__main__':
    s = Solution()
    print(s.find132pattern([-1, 3, 2, 0]))
