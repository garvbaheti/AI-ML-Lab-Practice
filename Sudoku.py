import numpy as np
import time
def check(puzz,r,c,n):
  #checking the number in rows and columns which it belong to
  for i in range(9):
    if puzz[r][i]==n:
      return False
  
  for i in range(9):
    if puzz[i][c]==n:
      return False
  #checking the number for the 3*3 Matrix to which it belongs
  x = r-r%3
  y = c-c%3
  for i in range(3):
    for j in range(3):
      if puzz[i+x][j+y]==n:
        return False
  return True
s=9
def sudoku(puzz,r,c):
  if(r==s-1 and c==s):
    return True
  if c==s:
    r+=1
    c=0
  if puzz[r][c]>0:
    return sudoku(puzz,r,c+1)
  for n in range(1,s+1,1):
    if check(puzz,r,c,n):
      puzz[r][c]=n
      if sudoku(puzz,r,c+1):
        return True
    puzz[r][c]=0
  return False

puzzle=np.array([[0,0,0,2,6,0,7,0,1], 
                 [6,8,0,0,7,0,0,9,0],
                 [1,9,0,0,0,4,5,0,0],
                 [8,2,0,1,0,0,0,4,0],
                 [0,0,4,6,0,2,9,0,0],
                 [0,5,0,0,0,3,0,2,8],
                 [0,0,9,3,0,0,0,7,4],
                 [0,4,0,0,5,0,0,3,6],
                 [7,0,3,0,1,8,0,0,0]])
print(puzzle)
print("--------------------")
start = time.time()
sudoku(puzzle,0,0)
end = time.time()
print(puzzle)
print("Execution Time:", end-start,"s")