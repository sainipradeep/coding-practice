class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    carry = 0
    index = len(digits)-1
    while index > -1:
      n = digits[index]
      if carry is 10:
        carry =1


