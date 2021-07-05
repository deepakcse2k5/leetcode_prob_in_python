from typing import List


matrix = [[1,2,3],[4,5,6],[7,8,9]]


N = len(matrix)
matrix.reverse()
print(matrix)
for r in range(N):
    for c in range(r):
        matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
print(matrix)
            
