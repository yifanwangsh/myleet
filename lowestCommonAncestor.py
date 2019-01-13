import unittest
def lowestCommonAncestor(root,p,q):
    def hasDescedent(head,node):
        left=False
        right=False
        if head.left:
            left = hasDescedent(head.left,node)
        if head.right:
            right = hasDescedent(head.right,node)
        return head.val==node.val or left or right
    
    head=root
    while hasDescedent(head,p) and hasDescedent(head,q):
        if head.left:
            left=hasDescedent(head.left,p) and hasDescedent(head.left,q)
        else:
            left=False
        if head.right:
            right = hasDescedent(head.right,p) and hasDescedent(head.right,q)
        else:
            right=False
        if left:
            head=head.left
        elif right:
            head=head.right
        else:
            return head 


class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Test(unittest.TestCase):
    def test1(self):
        t1=TreeNode(3)
        t2=TreeNode(5)
        t3=TreeNode(1)
        t4=TreeNode(6)
        t5=TreeNode(2)
        t6=TreeNode(0)
        t7=TreeNode(8)
        t8=TreeNode(7)
        t9=TreeNode(4)
        t1.left=t2
        t1.right=t3
        t2.left=t4
        t2.right=t5
        t3.left=t6
        t3.right=t7
        t5.left=t8
        t5.right=t9
        self.assertEqual(3,lowestCommonAncestor(t1,t2,t3).val)
    
    def test2(self):
        t1=TreeNode(1)
        t2=TreeNode(2)
        t1.left=t2
        self.assertEqual(1,lowestCommonAncestor(t1,t1,t2).val)

unittest.main()