class Solution:
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    final = []
    def permute(arr, index):
      final.append(arr)
      for i in range(index, len(nums)):
        if i!=index and nums[i] == nums[i-1]:
          continue
        permute(arr+[nums[i]], index+1)
    permute([], 0)
    return final
# [1, 2, 2]
# [4,4,4,1,4]
