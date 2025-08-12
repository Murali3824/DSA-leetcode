# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        q = deque([root])
        right_view = []

        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                
                # If this is the last node of the current level, add it to result
                if i == level_size - 1:
                    right_view.append(node.val)

                # Add children for next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return right_view



        # res = []
        # def dfs(node, depth):
        #     if not node:
        #         return

            # First time we visit this depth
        #     if depth == len(res):
        #         res.append(node.val)

            # Visit right first, then left
        #     dfs(node.right, depth + 1)
        #     dfs(node.left, depth + 1)

        