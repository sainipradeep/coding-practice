# import sys
# sys.setrecursionlimit(10 ** 6)
# def countCoinChange(coins, m, n):
#   if (n == 0):
#     return 1
#
#   if (n < 0):
#     return 0
#
#   if (m <= 0 and n >= 1):
#     return 0
#
#   return countCoinChange(coins, m - 1, n) + countCoinChange(coins, m, n - coins[m - 1])
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#       n = int(input())
#       coins = list(map(int , input().strip().split()))
#       m = int(input())
#       print(countCoinChange(coins,n, m))



def countCoinChange(coins, m, n):
  table = [0 for k in range(n + 1)]
  table[0] = 1
  for i in range(0, m):
    for j in range(coins[i], n + 1):
      # print(coins[i], j - coins[i], table[j - coins[i]])
      table[j] += table[j - coins[i]]
    print(table)
  return table[n]



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      n = int(input())
      coins = list(map(int , input().strip().split()))
      m = int(input())
      print(countCoinChange(coins,n, m))

# 1
# 4
# 2 5 3 6
# 10
