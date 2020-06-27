# User function Template for python3

def max_sum(a, n):
  cur_sum = 0
  curr_val = 0
  for i in range(len(a)):
    cur_sum += a[i]
    curr_val += i*a[i]
  res = curr_val
  for i in range(1, len(a)):
    next_val = (curr_val-(cur_sum-a[i-1])+a[i-1]*(n-1))
    curr_val = next_val
    res = max(curr_val, res)
  return res
  # print(cur_sum, curr_val)
# code here

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
  t = int(input())
  for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(max_sum(arr, n))
# } Driver Code Ends
