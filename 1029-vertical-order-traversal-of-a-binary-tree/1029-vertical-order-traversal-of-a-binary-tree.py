# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root):
        nodes = []  # (col, row, val)
        
        # BFS with coordinates
        queue = deque([(root, 0, 0)])  # (node, row, col)
        
        while queue:
            node, row, col = queue.popleft()
            if node:
                nodes.append((col, row, node.val))
                queue.append((node.left, row+1, col-1))
                queue.append((node.right, row+1, col+1))
        
        # Sort: col, then row, then value
        nodes.sort(key=lambda x: (x[0], x[1], x[2]))
        
        # Group by col
        col_table = defaultdict(list)
        for col, row, val in nodes:
            col_table[col].append(val)
        
        # Return in col order
        return [col_table[x] for x in col_table]

        