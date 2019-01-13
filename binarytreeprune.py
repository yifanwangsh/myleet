import unittest
def pruneTree(root):
    def checkSubtreeHasOne(node):
        if not (node.left or node.right):
            return node.val==1
        if not node.left and node.right:
            check = checkSubtreeHasOne(node.right)
            if not check:
                node.right=None
                return node.val==1
            return True        
        elif not node.right and node.left:
            check = checkSubtreeHasOne(node.left)
            if not check:
                node.left=None
                return node.val==1
            return True
        else:
            checkleft = checkSubtreeHasOne(node.left)
            checkright = checkSubtreeHasOne(node.right)
            if not checkleft:
                node.left=None
            if not checkright:
                node.right=None
            return checkleft or checkright

    checkSubtreeHasOne(root)
    return root

class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
    def setLeft(self,node):
        self.left=node
    def setRight(self,node):
        self.right=node

class TestMethod(unittest.TestCase):
    def test1(self):
        t1=TreeNode(1)
        t2=TreeNode(0)
        t3=TreeNode(0)
        t4=TreeNode(1)
        t1.setRight(t2)
        t2.setLeft(t3)
        t2.setRight(t4)
        result=pruneTree(t1)
        self.assertEqual(None,result.right.left)

    def test2(self):
        t1=TreeNode(1)
        t2=TreeNode(1)
        t3=TreeNode(0)
        t4=TreeNode(1)
        t5=TreeNode(1)
        t6=TreeNode(0)
        t7=TreeNode(1)
        t8=TreeNode(0)
        t1.setLeft(t2)
        t1.setRight(t3)
        t2.setLeft(t4)
        t2.setRight(t5)
        t3.setLeft(t6)
        t3.setRight(t7)
        t4.setLeft(t8)
        result=pruneTree(t1)
        self.assertEqual(None,result.left.left.left)
        self.assertEqual(None,result.right.left)

unittest.main()