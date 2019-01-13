import unittest
def numFactoredBinaryTree(A):
    dic={}
    A.sort()
    for i in range(0,len(A)):
        a=A[i]
        dic[a]=1
        for j in range(0,i):
            if a%A[j]==0 and a/A[j] in A:
                dic[a]+=dic[A[j]]*dic[a/A[j]]
    print (dic)
    return sum(i for i in dic.values())

class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class TestMethod(unittest.TestCase):
    def test1(self):
        self.assertEqual(3,numFactoredBinaryTree([2,4]))
    
    def test2(self):
        self.assertEqual(7,numFactoredBinaryTree([2,4,5,10]))
    
    def test3(self):
        self.assertEqual(12,numFactoredBinaryTree([18,3,6,2]))

    def test4(self):
        self.assertEqual(509730797,numFactoredBinaryTree([46,144,5040,4488,544,380,4410,34,11,5,3063808,5550,34496,12,540,28,18,13,2,1056,32710656,31,91872,23,26,240,18720,33,49,4,38,37,1457,3,799,557568,32,1400,47,10,20774,1296,9,21,92928,8704,29,2162,22,1883700,49588,1078,36,44,352,546,19,523370496,476,24,6000,42,30,8,16262400,61600,41,24150,1968,7056,7,35,16,87,20,2730,11616,10912,690,150,25,6,14,1689120,43,3128,27,197472,45,15,585,21645,39,40,2205,17,48,136]))

unittest.main()