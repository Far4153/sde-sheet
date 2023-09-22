matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60],[859,3647,3782,4000]]

target=3782

def searchMatrix( matrix, target) :
    n=len(matrix)
    m=len(matrix[0])

    low=0
    high=n*m-1

    while low<=high:
        mid=(low+high)//2
        row=mid//m
        col=mid%m
        if matrix[row][col]==target:
            return True
        elif mid>target:
            high=mid-1

        else:
            low=mid+1
    return False


print(searchMatrix(matrix,target))
        