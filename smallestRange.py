def smallestRange(A,K):
    min=A.pop(0)
    max=min
    while len(A)>0:
        a=A.pop(0)
        if a < min:
            min=a
        elif a > max:
            max=a
    diff=max-min-K*2
    if diff<0:
        return 0
    else:
        return diff

print (smallestRange([1],0))