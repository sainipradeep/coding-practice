class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    for i in range(len(nums) - 2, -1, -1):
      if nums[i] == nums[i + 1]:
        nums.pop(i)
