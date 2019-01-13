# from queue import Queue
from queue import Queue
import unittest
def zigzagorder(root):
    r=[]
    q=Queue()
    if root:
        q.put((root,1))
    while not q.empty():
        t=q.get()
        node=t[0]
        level=t[1]
        value = node.val
        if node.left:
            q.put((node.left,level+1))
        if node.right:
            q.put((node.right,level+1))

        if level==len(r):
            r[level-1].append(value)
        else:
            r.append([value])
            if level%2:
                r[level-2].reverse()
    if not len(r)%2 and root:
        r[len(r)-1].reverse()
    return r

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
        t6=TreeNode(4)
        t7=TreeNode(5)
        t1.left=t2
        t1.right=t3
        t3.left=t4
        t3.right=t5
        t2.left=t6
        t2.right=t7
        expected=[[3],[20,9],[4,5,15,7]]
        self.assertEqual(expected,zigzagorder(t1))

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
        expected=[[1],[2,2],[3,3],[4,4]]
        self.assertEqual(expected,zigzagorder(t1))

    def test3(self):
        self.assertEqual([],zigzagorder(None))

    def test4(self):
        t1=TreeNode(1)
        t2=TreeNode(2)
        t3=TreeNode(3)
        t1.left=t2
        t1.right=t3
        expected=[[1],[3,2]]
        self.assertEqual(expected,zigzagorder(t1))

unittest.main()