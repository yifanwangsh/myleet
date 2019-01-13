import unittest
def isSymmetric(root):
    def sym(leftNode,rightNode):
        if leftNode==None and rightNode==None:
            return True
        elif leftNode==None and not rightNode==None or not leftNode==None and rightNode==None:
            return False
        elif not leftNode.val==rightNode.val:
            return False
        return sym(leftNode.left,rightNode.right)*sym(leftNode.right, rightNode.left) 
    
    if root==None:
        return True
    elif root.left==root.right==None:
        return True    
    elif root.left==None and not root.right==None or root.right==None and not root.left==None:
        return False
    elif not root.left.val==root.right.val:
        return False
    else:
        return bool(sym(root.left.left, root.right.right)*sym(root.left.right, root.right.left))

class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
    def setLeft(self, node):
        self.left=node
    def setRight(self, node):
        self.right=node
    
class TestMethod(unittest.TestCase):
    def test1(self):
        t1=TreeNode(1)
        t2=TreeNode(2)
        t3=TreeNode(2)
        t4=TreeNode(3)
        t5=TreeNode(4)
        t6=TreeNode(4)
        t7=TreeNode(3)
        t1.setLeft(t2)
        t1.setRight(t3)
        t2.setRight(t5)
        t3.setLeft(t6)
        self.assertEqual(True,isSymmetric(t1))

    def test2(self):
        t1=TreeNode(1)
        t2=TreeNode(2)
        t3=TreeNode(2)
        t4=TreeNode(3)
        t5=TreeNode(3)
        t1.setLeft(t2)
        t1.setRight(t3)
        t2.setRight(t4)
        t3.setRight(t5)
        self.assertEqual(False,isSymmetric(t1))

    def test3(self):
        t1=TreeNode(1)
        t2=TreeNode(2)
        t3=TreeNode(3)
        t4=TreeNode(3)
        t5=TreeNode(2)
        t1.setLeft(t2)
        t1.setRight(t3)
        t2.setLeft(t4)
        t3.setLeft(t5)
        self.assertEqual(False,isSymmetric(t1))
    
    def test4(self):
        t1=TreeNode(9)
        t2=TreeNode(-42)
        t3=TreeNode(-42)
        t4=TreeNode(76)
        t5=TreeNode(76)
        t6=TreeNode(13)
        t7=TreeNode(13)
        t1.setLeft(t2)
        t1.setRight(t3)
        t2.setRight(t4)
        t3.setLeft(t5)
        t4.setRight(t6)
        t5.setRight(t7)
        self.assertEqual(False,isSymmetric(t1))

unittest.main()