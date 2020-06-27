class Solution:
  def addDigits(self, num: int) -> int:
    if num <= 9:
      return num
    sum = 0
    while num>0:
      sum += num % 10
      num = int(num / 10)

    return self.addDigits(sum)


if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(59))
