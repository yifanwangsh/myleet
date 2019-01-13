import unittest
def preorderTraversal(root):
    out=[]
    while root:
        if root.right and root.left:
            curr=root.left
            while curr.right:
                curr=curr.right
            curr.right=root.right
        out.append(root.val)
        if root.left:
            root=root.left
        else:
            root=root.right                
    return out           



class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class TestMethod(unittest.TestCase):
    def test1(self):
        t1=TreeNode(3)
        t2=TreeNode(9)
        t3=TreeNode(20)
        t4=TreeNode(15)
        t5=TreeNode(7)
        t1.left=t2
        t1.right=t3
        t3.left=t4
        t3.right=t5
        expected=[3,9,20,15,7]
        self.assertEqual(expected,preorderTraversal(t1))

    def test2(self):
        t1=TreeNode(1)
        t2=TreeNode(2)
        t3=TreeNode(2)
        t4=TreeNode(3)
        t5=TreeNode(3)
        t6=TreeNode(4)
        t7=TreeNode(4)
        t1.left=t2
        t1.right=t3
        t2.left=t4
        t2.right=t5
        t4.left=t6
        t4.right=t7
        expected=[1,2,3,4,4,3,2]
        self.assertEqual(expected,preorderTraversal(t1))

    def test3(self):
        self.assertEqual([],preorderTraversal(None))

unittest.main()