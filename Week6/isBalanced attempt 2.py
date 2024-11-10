# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        
        # quick leave because given none root
        if root is None:
            return True
        
        #the code to calculate the height 
        def BSTGetHeight(node) : 
            if (node is None) :
                return -1
            
            leftHeight = BSTGetHeight(node.left)
            rightHeight = BSTGetHeight(node.right)
            return 1 + max(leftHeight, rightHeight)
        
        # instead of looking for tallist branch, looks for shortest
        def BSTGetminHeight(node) : 
            if (node is None) :
                return -1
            
            leftHeight = BSTGetHeight(node.left)
            rightHeight = BSTGetHeight(node.right)
            return 1 + min(leftHeight, rightHeight)
            
        tall =  (BSTGetHeight(root))
        short =  (BSTGetminHeight(root))
        #compares the 2 branches and returns base of if different hieghts 
        return tall - short <= 1