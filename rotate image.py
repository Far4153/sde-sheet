matrix=[[1,2,3],[4,5,6],[7,8,9]]

for c in range(len(matrix)):
    for r in range(c):
        matrix[c][r],matrix[r][c]=matrix[r][c],matrix[c][r]
    # print(matrix)

for i in matrix:
    i.reverse()


print(matrix)