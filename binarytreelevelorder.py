import queue
import unittest
def levelOrder(root):
    traverse=[]
    q=queue.Queue(-1)
    if root:
        q.put((root,1))
    while not q.empty():
        t=q.get()
        node=t[0]
        level=t[1]
        if node.left:
            q.put((node.left,level+1))
        if node.right:
            q.put((node.right,level+1))
        
        if len(traverse)==level:
            traverse[level-1].append(node.val)
        else:
            traverse.append([node.val])
    return traverse

class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Test(unittest.TestCase):
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
        expected=[[3],[9,20],[15,7]]
        self.assertEqual(expected,levelOrder(t1))

unittest.main()
        