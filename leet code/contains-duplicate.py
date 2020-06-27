class Solution:
  def containsDuplicate(self, nums) -> bool:
    hash = {}

    for i in nums:
      if i in hash:
        return 1
      hash[i] = 1
    return 0

if __name__ == '__main__':
    a = Solution()
    print(a.containsDuplicate([1,2,3,1]))
