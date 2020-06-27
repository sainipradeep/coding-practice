import math
if __name__ == "__main__":
  t = int(input())

  while (t > 0):
    string = input()
    arr = []

    if len(string)%2:
      print(-1)

    for s in string:
      if s is '}':
        if len(arr)>0 and arr[-1] is "{":
          arr.pop()
        else:
          arr.append(s)
      else:
        arr.append(s)



    n = 0

    while len(arr)>0 and arr[0]  is '{':
      n+=1
      arr.pop()
    print(len(string), n)
    print(math.ceil(len(string)/2) +math.ceil(n%2))





