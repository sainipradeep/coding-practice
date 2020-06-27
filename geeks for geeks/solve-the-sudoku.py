def solveSudoku(sudoku):
  positions = [0, 0]
  if not getEmptyIndex(sudoku, positions):
    return 1

  row = positions[0]
  col = positions[1]

  for i in range(1, 10):
    if try_to_place_a_number_at_position(sudoku, i, row, col):
      sudoku[row][col] = i

      if solveSudoku(sudoku):
        return 1

      sudoku[row][col] = 0
  return 0

def try_to_place_a_number_at_position(sudoku, num, row, col):
  return not used_in_row(sudoku, num, row) \
         and  not used_in_col(sudoku, num, col) and\
        not used_in_box(sudoku, num, row-row%3, col-col%3)

def used_in_row(sudoku, num, row):
  for i in range(9):
    if sudoku[row][i] == num:
      return 1
  return

def used_in_col(sudoku, num, col):
  for i in range(9):
    if sudoku[i][col] == num:
      return 1
  return 0

def used_in_box(sudoku,num, row, col):
  for i in range(3):
    for j in range(3):
      try:
        if sudoku[row + i][col + j] == num:
          return 1
      except NameError:
        print(NameError, i , j, row, col)
  return 0

def getEmptyIndex(sudoku, positions):
  for i in range(9):
    for j in range(9):
      if sudoku[i][j] == 0:
        positions[0] = i
        positions[1] = j
        return 1
  return 0

def printSudoku(sudoku):
  for i in range(9):
    for j in range (9):
      print(sudoku[i][j], end=" ")
  print()

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      sudoku = [[0 for i in range(9)] for  i in range(9)]
      a =0
      queue = list(map(int, input().strip().split()))
      for i in range(9):
        for j in range(9):
          sudoku[i][j]= queue[a]
          a+=1

      # sudoku = list(map(list, zip(*[map(int, input().strip().split())] * 9)))
      solveSudoku(sudoku)
      printSudoku(sudoku)



