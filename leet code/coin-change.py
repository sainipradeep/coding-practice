class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    table = [0] + [float('inf') for i in range(amount)]
    for i in range(amount+1):
      for coin in coins:
        if i -coin >=0:
          table[i] = min(table[i], table[i-coin]+1)

    if table[-1] == float('inf'):
      return -1
    return table[-1]



if __name__ == '__main__':
    a = Solution()
    a.coinChange([1, 2, 5], 11)
