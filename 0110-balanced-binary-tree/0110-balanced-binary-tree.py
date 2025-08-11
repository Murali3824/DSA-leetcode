# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Returns True if the binary tree is height-balanced.
        """

        def check_height(node):
            # An empty node has height 0
            if not node:
                return 0

            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1:  # Left subtree is unbalanced
                return -1

            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1:  # Right subtree is unbalanced
                return -1

            # If current node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1

            # Height of current node
            return 1 + max(left_height, right_height)

        # Tree is balanced if check_height does not return -1
        return check_height(root) != -1
