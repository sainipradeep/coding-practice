#User function Template for python3

def countWays(m):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''
    mod = 1000000007
    # code here
    arr = [0 for i in range(m+1)]
    arr[0] = 1
    arr[1] = 1

    for i in range(2, m+1):
      if i%2 is 0:
        arr[i] = arr[i - 1] + 1
      else:
        arr[i] = arr[i - 1]

    return arr[m]



#{
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        print(countWays(m))

# } Driver Code Ends
