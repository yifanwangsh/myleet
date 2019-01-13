def minMoves(nums):
    m=min(nums)
    return sum(x-m for x in nums)

print (minMoves([1,2,3]))
print (minMoves([1,2147483647]))