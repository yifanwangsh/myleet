def searchMatrix(matrix,target):
    m=len(matrix)
    if m==0:
        return False
    n=len(matrix[0])
    row=-1
    for i in range(0,m):
        if i+1<=m-1 and matrix[i][0]<=target and matrix[i+1][0]>target:
            row=i
    if row==-1:
        row=m-1
    for i in range(0,n):
        if matrix[row][i]==target:
            return True
    return False


matrix=[
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,50]
]
target=13
print (searchMatrix(matrix,target))

matrix=[[1]]
target=1
print (searchMatrix(matrix,target))
