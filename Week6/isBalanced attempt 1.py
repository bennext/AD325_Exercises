# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        list_of_depths = [0]
        if root is None:
            return True
        
        def recur (local_root):
            
            list_of_depths[-1] += 1
            
            if not(local_root.left is None):
                # list_of_depths.append(0)
                recur (local_root.left)

            if not(local_root.right is None): 
                # list_of_depths.append(0) 
                recur (local_root.right)

            if local_root.left is None and local_root.right is None:
                list_of_depths.append(list_of_depths[-1]-1) 

        recur(root)

        print (list_of_depths)

        return list_of_depths