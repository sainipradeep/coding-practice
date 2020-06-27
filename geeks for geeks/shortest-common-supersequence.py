def find_lcs_count(str1, str2):
  dp = [[0 for i in range(len(str1)+1)] for i in range(len(str2)+1)]


  for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
      print(j)
      if str1[i-1] == str2[j-1]:
        dp[i][i] = 1+ dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

  print(dp)
  # for i in range(len(dp[0])):
  #   dp[0][i] = 1
  # for i in range(len(dp)):
  #   dp[i][0] = 1




  return

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      strs = input().strip().split()
      print(find_lcs_count(strs[0], strs[1]))
