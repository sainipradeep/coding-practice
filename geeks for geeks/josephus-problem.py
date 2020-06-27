# {
# Driver Code Starts
import math


# } Driver Code Ends

# Complete this function
def josephus(n, k):
  if n<=0:
    return 0

  return ((josephus(n-1, k)+k-1)%n+1)
  # if n <= 0:
  #   return 0
  #
  # circle = [i for i in range(1, n+1)]
  # start_index = k-1
  # while len(circle)>1:
  #   n = len(circle)
  #   circle.pop(start_index)
  #   if start_index+ k >= n:
  #     start_index = start_index+ k - n
  #   else:
  #     start_index += k
  # return circle[0]

# {
# Driver Code Starts.

def main():
  T = int(input())

  while (T > 0):
    nk = [int(x) for x in input().strip().split()]
    n = nk[0]
    k = nk[1]

    print(josephus(n, k))

    T -= 1


if __name__ == "__main__":
  main()
# } Driver Code Ends
