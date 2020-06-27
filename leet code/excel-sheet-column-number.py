# class Solution:
#   def convertToTitle(self, n: int) -> str:
#     result = ''
#     while n:
#       result += chr((n - 1) % 26 + ord('A'))
#       n = (n - 1) // 26
#     return result[::-1]
#     # hash = {
#     #   1: 'A',
#     #   2: 'B',
#     #   3: 'C',
#     #   4: 'D',
#     #   5:'E',
#     #   6:'F',
#     #   7:'G',
#     #   8:'H',
#     #   9:'I',
#     #   10:'J',
#     #   11:'K',
#     #   12:'L',
#     #   13:'M',
#     #   14:'N',
#     #   15:'O',
#     #   16:'P',
#     #   17:'Q',
#     #   18:'R',
#     #   19:'S',
#     #   20:'T',
#     #   21:'U',
#     #   22:'V',
#     #   23:'W',
#     #   24:'X',
#     #   25:'Y',
#     #   26:'Z'
#     # }
#     #
#     #
#     # if n <= 26:
#     #   return hash[n]
#     # last = ((n-1 )% 26) + 1
#     #
#     # temp = 0
#     # output = ""
#     # n -=26
#     # while n > 0:
#     #   temp += 1
#     #   n -= 26
#     #   # if temp >= 26:
#     #     # output = output + hash[26]
#     #     # temp = 0
#     #
#     # while temp > 0:
#     #
#     #   output = output + hash[((temp-1)%26)+1]
#     #   temp-=26
#     #
#     # output += hash[last]
#     # return output
#
# if __name__ == '__main__':
#   a = Solution()
#   print(a.convertToTitle(701))
#   print(a.convertToTitle(703))
#   print(a.convertToTitle(1048))
#   print(a.convertToTitle(500))
#


class Solution:
  def titleToNumber(self, s: str) -> int:
    output = 0
    for i in range(len(s)):
      output *=26
      output += ord(s[i])- ord('A')+1
    return output
