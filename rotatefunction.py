def maxRotateFunction(A):
    n=len(A)
    s=sum(A)
    base=0
    final=0
    for i in range(n):
        base+=A[i]*i
        final=base
    for j in range(1,n):
        base+=s-n*A[n-j]
        if base>final:
            final=base
    return final
    

print (maxRotateFunction([4,3,2,6]))