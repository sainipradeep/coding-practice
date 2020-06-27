class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return 0

    temp, reverse = x, 0

    while temp:
      reverse *=10
      reverse += temp%10
      temp //=10
    return reverse == x
