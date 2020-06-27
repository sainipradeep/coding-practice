class Solution:
  def reverse(self, x: int) -> int:
    negetive = x < 0
    reverse = 0
    if negetive:
      x *=-1
    while x:
      reverse *= 10
      reverse += x%10
      x //= 10

    if reverse > (2**31)-1:
      return 0
    if negetive:
      return -reverse
    return reverse
    # print(reverse)

if __name__ == '__main__':
   a = Solution()
   a.reverse(-123)
