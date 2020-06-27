class Solution:
  def minSteps(self, n: int) -> int:
    if n <= 0:
      return 0

    output = 0
    s1 = 1
    s2 = 1
    for i in range(1, n):

    if n%2 is not 0:
      output += s2

if __name__ == '__main__':
    a  = Solution()
    a.minSteps(3)
