# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#       n = int(input())
#       if n%2 is 0:
#         print(1)
#       else:


#         print(0)


# class Solution:
#   def isHappy(self, n: int) -> bool:
#     if n <= 0:
#       return 0
#     if n is 1 or n is 7:
#       return 1
#
#     arr = list(map(int, str(n)))
#     next_number = 0
#     for i in arr:
#       next_number += i*i
#
#     if next_number is 7:
#       return 1
#     if next_number>9:
#       return isHappy(next_number)
#
#     return false



#Product of all Subarrays of an Array
if __name__ == '__main__':
    # arr = [2, 4]
    # n = 2
    arr = [10, 3, 7]
    n = 3
    product = 1
    for i in range(n):
      for j in range(i, n):
        product = product * arr[j]

    print(product)



