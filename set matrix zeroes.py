


def setZeroes( matrix):
    m= len(matrix)
    n= len(matrix[0])

        
    zeroIndexArr=[]

    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                zeroIndexArr.append([i,j])
    for a,b in zeroIndexArr:
        for r in range(n):
            matrix[a][r]=0
        for c in range(m):
            matrix[c][b]=0



            