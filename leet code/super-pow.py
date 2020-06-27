class Solution:
  def superPow(self, a: int, b: List[int]) -> int:
    t = 0
    for i in b:
      t +=i*10
      t +=i
    return pow(a, t)
