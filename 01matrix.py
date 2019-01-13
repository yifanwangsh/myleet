def updatematrix(matrix):
    m=len(matrix)
    if not m==0:
        n=len(matrix[0])
    else:
        return [[]]
    
    new=[]
    for i in range(m):
        r=[]
        for j in range(n):
            if matrix[i][j]==0:
                r.append(0)
            else:
                r.append(None)
        new.append(r)
    
    def fill(num):
        re=[]
        for i in range(m):
            r=[]
            for j in range(n):
                if isinstance(new[i][j], int):
                    r.append(new[i][j])
                else:
                    if i>=1:
                        up=new[i-1][j]
                    else:
                        up=None
                    try:
                        down=new[i+1][j]
                    except IndexError:
                        down=None
                    if j>=1:
                        left=new[i][j-1]
                    else:
                        left=None
                    try:
                        right=new[i][j+1]
                    except IndexError:
                        right=None
                    if up==num-1 or down==num-1 or left==num-1 or right==num-1:
                        r.append(num)
                    else:
                        r.append(None)
            re.append(r)
        return re
    def hasnone():
        for r in new:
            if None in r:
                return True
        return False
    level=1
    while hasnone():
        new=fill(level)
        level+=1
    return new
    # new=fill(1)
    # # new=fill(2)

# print (updatematrix([[0,0,0],[0,1,0],[1,1,1]]))
print (updatematrix([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], 
                     [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], 
                     [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], 
                     [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], 
                     [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], 
                     [0, 0, 1, 0, 1, 1, 1, 0, 1, 0], 
                     [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], 
                     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], 
                     [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], 
                     [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]))