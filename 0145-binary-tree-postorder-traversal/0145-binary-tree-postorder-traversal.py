# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inord(node):
            if not node:
                return
            inord(node.left)
            inord(node.right)
            res.append(node.val)
        inord(root)
        return res

        # using iterative stack 1
        # res = []
        # if not root:
        #     return []
        # stack = [root]

        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)

        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return res[::-1]


        # using iterative stack 2
        # if not root:
        #     return []
        
        # stack1 = [root]
        # stack2 = []
        # res = []
        
        # while stack1:
        #     node = stack1.pop()
        #     stack2.append(node)
            
        #     if node.left:
        #         stack1.append(node.left)
        #     if node.right:
        #         stack1.append(node.right)

        # while stack2:
        #     node = stack2.pop()
        #     res.append(node.val)
        
        # return res