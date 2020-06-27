# # # # def maxSumArray(arr, n):
# # # #   dp = [arr[0]]
# # # #
# # # #   for i in range(1, n):
# # # #     dp.append( max(arr[i], dp[i-1] + arr[i]))
# # # #
# # # #   return max(dp)
# # # #
# # # # if __name__ == '__main__':
# # # #     t = int(input())
# # # #     for _ in range(t):
# # # #       n = int(input())
# # # #       arr = list(map(int, input().strip().split()))
# # # #       print(maxSumArray(arr, n))
# # # #
# # # #
# # #
# # #
# # # def solution(N):
# # #   # write your code in Python 3.6
# # #   b_num = bin(N)
# # #   b_num = b_num[2:]
# # #   max_num = 0
# # #   temp_max = 0
# # #   for i in range(len(b_num)):
# # #     # print(b_num[i])
# # #     if b_num[i] is '1':
# # #       if temp_max > max_num:
# # #         max_num = temp_max
# # #       temp_max = 0
# # #     else:
# # #       temp_max += 1
# # #     if temp_max > max_num:
# # #       max_num = temp_max
# # #   return max_num
# # #
# # # if __name__ == '__main__':
# # #   print(solution(32))
# #
# #
# # # you can write to stdout for debugging purposes, e.g.
# # # print("this is a debug message")
# #
# # def solution(N, S):
# #   # write your code in Python 3.6
# #
# #   output = 0
# #   map = {}
# #   arr = []
# #   if len(S.strip())>0:
# #     arr = list(S.split(" "))
# #
# #   for i in range(1, N+1):
# #     row = []
# #     a = [0]*3
# #     b = [0]*3
# #     c = [0]*3
# #     row.append(a)
# #     row.append(b)
# #     row.append(c)
# #     map[i] = row
# #     if len(S.strip())>0:
# #       for j in arr:
# #         str = j
# #         subStr = str[:1]
# #         curRow = int(str[0:1])
# #         if curRow is i:
# #           if subStr is "A":
# #             map.get(i)[0][0]= 1
# #           elif subStr is "B":
# #             map.get(i)[0][1]= 1
# #           elif subStr is "C":
# #             map.get(i)[0][2]= 1
# #           elif subStr is "D":
# #             map.get(i)[1][0]= 1
# #           elif subStr is "E":
# #             map.get(i)[1][1]= 1
# #           elif subStr is "F":
# #             map.get(i)[1][2]= 1
# #           elif subStr is "G":
# #             map.get(i)[1][3]= 1
# #           elif subStr is "H":
# #             map.get(i)[2][0]= 1
# #           elif subStr is "J":
# #             map.get(i)[2][1] = 1
# #           elif subStr is "K":
# #             map.get(i)[2][2] = 1
# #
# #   for i in range(1, N+1):
# #     if map[i][1] is  not 1:
# #       output+=1
# #     if map[i][1]is not 1:
# #       output +=1
# #     elif map[i][1] is 0 and map[i][1][2] is 0:
# #       if map[i][1][0] is 0 or map[i][1][3] is 0:
# #         output+=1
# #     if map[i][2] is 1:
# #       output+=1
# #
# #   return output
# #
# #
# #
# #
# # if __name__ == '__main__':
# #     solution(4, "1A 2F 1C 4A 3D 4C 3C 2G 4K")
#
#
# def solution(N: int, S: str, n:int) -> int:

#   """
#   return option count
#   """
#   taken = [[] for _ in range(N)]
#   for s in S.split(" "):
#     row = int(s[:-1]) - 1
#     if row > N:
#       raise Exception("illegal reservation")
#
#     taken[row].append(ord(s[-1]) - ord('A'))
#
#   total_cnt = 0
#   for row in taken:
#     row.sort()
#     row.append(ord('K') - ord('A') + 1)
#     last = -1
#
#     cnt = 0
#     for idx in range(len(row)):
#       free_seats = row[idx] - last - 1
#       cnt += max(0, free_seats - (n - 1))
#       last = row[idx]
#
#     total_cnt += cnt
#
#   return total_cnt
#
# if __name__ == '__main__':
#   solution(40, "1A 3C 2B 40G 5A", 40)


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task


def solution(T):
  if T is None:
    return 0
  return distinctPathMaxSize(T, {}, 1)
# write your code in Python 3.6


# {
#   x:10,
#   r:None,
#   l:None
# }
def distinctPathMaxSize(root, map, num):
  if root is None:
    return num

  if map.get(root.x) is None:
    if root.l is not None and map.get(root.l.x) is None:
      map[root.x] = 1

      num += 1
      l1 = distinctPathMaxSize(root.l, map, num)
    if root.r is not None and map.get(root.r.x) is None:
      map[root.x] = 1
      num += 1
      l2 = distinctPathMaxSize(root.r, map, num)
  del map[root.x]
  return max(l1, l2, num)

