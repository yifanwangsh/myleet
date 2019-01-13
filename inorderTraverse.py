import unittest
def inorderTraversal(root):
    r=[]
    curr=root
    while curr:
        if not curr.left:
            r.append(curr.val)
            curr=curr.right
        else:
            tmp=curr.left
            while tmp.right:
                tmp=tmp.right
            tmp.right=curr
            curr=curr.left
    return r       



class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
    def setLeft(self,node):
        self.left=node
    def setRight(self,node):
        self.right=node

class Test(unittest.TestCase):
    def test1(self):
        n1=TreeNode(1)
        n2=TreeNode(2)
        n3=TreeNode(3)
        n4=TreeNode(4)
        n5=TreeNode(5)
        n6=TreeNode(6)
        n1.setLeft(n2)
        n1.setRight(n3)
        n2.setLeft(n4)
        n2.setRight(n5)
        n3.setLeft(n6)
        self.assertEqual([4,2,5,1,3,6],inorderTraversal(n1))

unittest.main()