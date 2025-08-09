class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c, idx):
            # If all characters matched
            if idx == len(word):
                return True
            
            # Check boundaries and character match
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[idx]:
                return False
            
            # Mark the cell as visited by replacing with '#'
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore neighbors
            found = (backtrack(r+1, c, idx+1) or
                     backtrack(r-1, c, idx+1) or
                     backtrack(r, c+1, idx+1) or
                     backtrack(r, c-1, idx+1))
            
            # Restore the cell after exploration (backtracking)
            board[r][c] = temp
            
            return found
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # start DFS if first char matches
                    if backtrack(i, j, 0):
                        return True
        return False
