import unittest
def isBalanced(root):
    def balanced(node):
        if node.left and node.right:
            left=balanced(node.left)
            right=balanced(node.right)
            if left>=0 and right>=0 and abs(left-right) <= 1:
                return max(left,right)+1
            else:
                return -1
        elif not node.left and node.right:
            if balanced(node.right)==0:
                return 1
            else:
                return -1
        elif node.left and not node.right:
            if balanced(node.left)==0:
                return 1
            else:
                return -1
        else:
            return 0
    if root:
        return balanced(root)>=0
    else:
        return True
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
        self.assertEqual(True,isBalanced(t1))

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
        self.assertEqual(False,isBalanced(t1))

    def test3(self):
        self.assertEqual(True,isBalanced(None))

    def test4(self):
        t1=TreeNode(1)
        t2=TreeNode(2)
        t1.left=t2
        self.assertEqual(True,isBalanced(t1))

    def test5(self):
        t1=TreeNode(1)
        t2=TreeNode(2)
        t1.left=t2
        self.assertEqual(True,isBalanced(t1))

unittest.main()