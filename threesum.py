def threeSum(nums):
    cl = nums.copy()
    r = []
    check = []
    while (len(cl)>0):
        first = cl.pop(0)
        dic = {}
        for i in range(0, len(cl)):
            if (cl[i] not in dic.keys()):
                dic[0-first-cl[i]] = cl[i]
            else:
                triple = [first, cl[i], dic[cl[i]]]
                settriple = set(triple)
                if (settriple not in check):
                    r.append(triple)
                    check.append(set(triple))
                dic.pop(cl[i])

    return r

input = [-1,0,1,2,-1,-4,-2,-3,5,6,7,-3,-1]
print (threeSum(input))