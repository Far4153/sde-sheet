matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60],[859,3647,3782,4000]]

target=3782

def searchMatrix( matrix, target) :
    rowend=len(matrix[0])-1
    rowstart=0

    while rowstart<len(matrix)-1:
        if matrix[rowstart][rowend]<target:
            rowstart+=1
        else:
            break

    for i in range(0,len(matrix[0])):
        # print(rowstart,i)
        if matrix[rowstart][i]==target:
            return True
        
    return False


    

print(searchMatrix(matrix,target))