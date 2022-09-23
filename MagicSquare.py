import numpy as np

def magicSquare(N):
  magic_square = np.zeros((N,N), dtype=int)
  n = 1
  i= 0
  j=N//2

  while n <= N**2:
      magic_square[i, j] = n
      n += 1
      x = (i-1) % N 
      y = (j+1) % N
      if magic_square[x, y]:
          i += 1
      else:
          i = x
          j = y
  return (magic_square)
N  = int(input("Enter a Odd Number: "))
if N%2==0:
  print("Not Odd Number")
else:
  print(magicSquare(N))
