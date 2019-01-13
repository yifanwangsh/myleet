def singleNumber(nums):
    exist=[]
    for i in nums:
        if i in exist:
            exist.remove(i)
        else:
            exist.append(i)
    return exist

print (singleNumber([1,2,1,3,2,5]))