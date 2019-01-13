def uniquePaths(m,n):
    path=0
    def next(x,y):
        nonlocal path 
        if x==m-1 and y==n-1:
            path += 1
            return 
        elif x==m-1: 
            next(x,y+1)
        elif y==n-1:
            next(x+1,y)
        else:
            next(x+1,y)
            next(x,y+1)
    
    next(0,0)
    
    return path
print (uniquePaths(23,12))    