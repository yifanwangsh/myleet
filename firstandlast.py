# def searchRange(nums, target):
#     l1 = nums.copy()
#     o1=[]
#     o2=[]
#     for i in range(0, len(nums)):
#         o1.append(i)
#         o2.append(i)
#     #find first
#     while (len(l1)>1):
#         if (target < l1[int(len(l1)/2)]):
#             l1 = l1[:int(len(l1)/2)]
#             o1 = o1[:int(len(o1)/2)]
#         else:
#             l1 = l1[-int(len(l1)/2):]
#             o1 = o1[-int(len(o1)/2):]
#     return o1
#     #find last

# print (searchRange([5,7,7,8,8,8,10],3))