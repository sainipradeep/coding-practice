class Solution:
  def subsets(self, nums):
    s = [[]]
    for i in nums:
      s += [j + [i] for j in s]
    return s

if __name__ == '__main__':
    a = Solution()
    print(a.subsets([1, 2, 3]))
