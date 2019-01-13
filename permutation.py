def permutation(nums):
    
    def subpermute(n, listOflist):
        pool = []
        for l in listOflist:
            for i in range(0,len(l)+1):
                newl = l.copy()
                newl.insert(i,n)
                pool.append(newl)
        return pool

    r =[[]]
    for n in range(0,len(nums)):
        r = subpermute(nums[n],r)

    return r



print (permutation([1,2,3,4]))
    