import unittest
def search(nums,target):
    if len(nums)==0:
        return -1
    i=int(len(nums)/2)
    mid=nums[i]
    if mid==target:
        return i
    elif mid>target:
        index = search(nums[:i],target)
        return index if index>=0 else -1
    else:
        index = search(nums[i+1:],target)
        return index+1+i if index>=0 else -1

# def search(nums,target):
#     half=0
#     def binary(begin,end):
#         if (begin+end)%2==0:
#             half=int((begin+end)/2)
#         else:
#             half=int((begin+end)*0.5+0.5)
#         get=nums[half]
#         if target==nums[begin]:
#             return begin
#         elif target==nums[end]:
#             return end
#         elif target==get:
#             return half
#         elif begin==end:
#             return -1
#         elif target<get:
#             return binary(begin,half-1)
#         elif target>get:
#             return binary(half,end)
#     return binary(0,len(nums)-1)

class TestMethod(unittest.TestCase):
    def test1(self):
        nums=[-1,0,3,5,9,12]
        target = 9
        self.assertEqual(4,search(nums,target))

    def test2(self):
        nums=[-1,0,3,5,9,12]
        target = 2
        self.assertEqual(-1,search(nums,target))

    def test3(self):
        nums=[-1,3,4,5,6,10,98]
        target=98
        self.assertEqual(6,search(nums,target))

unittest.main()