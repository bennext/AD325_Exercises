# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        # quick leave because given none root
        if root is None:
            return True
        
        self.balanced_so_far = True

        # compares the height of left vs right recursively 
        def internal(node):         

            if node is None:
                return 0

            left = internal(node.left)

            right = internal(node.right)

            if (abs(left - right) > 1):
                self.balanced_so_far = False

            return max(left, right) + 1

        internal(root)       
        return self.balanced_so_far