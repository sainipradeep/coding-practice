class Solution:
  def removeDuplicates(self, nums) -> int:
# class Solution:
#   def removeDuplicates(self, nums: List[int]) -> int:
    last = None
    occurrence = 0
    print(occurrence is None)
    for i in range(len(nums)-1, -1, -1):

      if not last or last != nums[i]:
        last = nums[i]
        occurrence = 1
      elif last == nums[i] and occurrence+1 > 2:
        nums.pop(i)
      else:
        occurrence+=1

if __name__ == '__main__':
    s = Solution()
    # s.removeDuplicates([0,0,1,1,1,1,2,3,3])
    s.removeDuplicates([0,0,0,0,0])






