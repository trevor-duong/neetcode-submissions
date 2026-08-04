# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recurse down left and right. the diameter is the Max(left, right) + 1
        # The base case is if there are no children, then the diameter is zero
        # left is diameterOfBinaryTree(left) + 1, right is the same with the right

        soln = 0
        def recurseChild (node: Optional[TreeNode]) -> int:
            nonlocal soln
            if node == None:
                return 0
        
            leftHeight = recurseChild(node.left)
            rightHeight = recurseChild(node.right)

            calculatedDiameter = leftHeight + rightHeight
            soln = max(soln, calculatedDiameter)

            return max(leftHeight, rightHeight) + 1

        if root == None:
            return soln
        recurseChild(root)
        return soln
        
       