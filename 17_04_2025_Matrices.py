

'''MATRICES : '''
mat1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
sum = 0

for i in mat1:
  # print(i) 
  for j in i:
    sum += j
  print(sum) 

# print(sum)  # 45

# print(mat1[1][2])



''' print only diagonal elements of a matrix'''

mat1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
    
    # Main Diagonal Condition: i == j checks for elements where the row index equals the column index

for i in range(len(mat1)):
  for j in range(len(mat1[i])):
    if i ==j: 
      print(mat1[i][j], end=' ')
    else:
      print(' ', end=' ')
  print()

''' print both diagonal elements of a matrix'''
# code for a square matrix: 3 * 3
mat1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
    # Anti-Diagonal Condition: i + j == len(mat1) - 1 ensures that the sum of the row and column indices equals the last index (for a 3x3 matrix, this is 2).

for i in range(len(mat1)):
  for j in range(len(mat1[i])):
    if i ==j or i + j == len(mat1)-1:
      print(mat1[i][j], end=' ')
    else:
      print(' ', end=' ')
  print()


''' print both diagonal elements of a matrix 4* 4 matrix and print the sum of the diagonals: '''
mat1 = [
  [1, 2, 3, 4],
  [4, 5, 6, 7],
  [7, 8, 9, 10],
  [11, 12, 13, 14]
]

sum=0
for i in range(len(mat1)):
  for j in range(len(mat1[i])):
    if i == j or i + j == len(mat1)-1:
      sum+=mat1[i][j]
      print(mat1[i][j], end=' ')
    else:
      print(' ', end=' ')
  print()
print(sum)

''' print the border elements of  a matrix: '''
mat1 = [
  [1, 2, 3, 4],
  [4, 5, 6, 7],
  [7, 8, 9, 1],
  [9, 3, 8, 1]
]

for i in range(len(mat1)):
  for j in range(len(mat1[i])):
    if i == 0 or j == 0 or i==len(mat1)-1 or j== len(mat1)-1 :
      print(mat1[i][j], end=' ')
    else:
      print(' ', end=' ')
  print()

''' print the sum of two matrixes of same order m * n'''
mat1 = [
  [1, 2, 3, 4],
  [4, 4, 4, 7],
  [5, 1, 2, 1],
  [1, 3, 5, 1]
]
mat2 = [
  [1, 2, 3, 4],
  [4, 5, 4, 2],
  [1, 5, 4, 1],
  [3, 3, 2, 1]
]

for i in range(len(mat1)):
  for j in range(len(mat1[j])):
    print(mat1[i][j] + mat2[i][j], end =' ')
  print()


''' print the sum of matrix in a new matrix '''

mat1 = [
  [1, 2, 3, 4],
  [4, 4, 4, 7],
  [5, 1, 2, 1],
  [1, 3, 5, 1]
]
mat2 = [
  [1, 2, 3, 4],
  [4, 5, 4, 2],
  [1, 5, 4, 1],
  [3, 3, 2, 1]
]

mat3 = []

for i in range(len(mat1)):
  mat3.append([])
  for j in range(len(mat1[i])):
    mat3[-1].append(mat1[i][j] + mat2[i][j])
  print()

print(mat3)

''' Transpose of a matrix: can be done on a square matrix only'''

mat1 = [
  [1, 2, 3, 4],
  [4, 4, 4, 7],
  [5, 1, 2, 1],
  [1, 3, 5, 1]
]

for i in range(len(mat1)):
  for j in range(len(mat1[i])):
    if i > j:
      mat1[i][j], mat1[j][i] = mat1[j][i], mat1[i][j]
    print(mat1[i][j])

print(mat1)