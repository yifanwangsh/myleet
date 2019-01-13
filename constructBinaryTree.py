def buildTree(preorder,inorder):

    root = preorder.pop(0)
    i = inorder.find(root)
    left = inorder[:i]
    right = inorder[i+1:]
    
    
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None