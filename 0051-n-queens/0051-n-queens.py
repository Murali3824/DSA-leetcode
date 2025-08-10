class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        board = [-1] * n
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        
        def backtrack(row):
            if row == n:
                solution = []
                for i in range(n):
                    solution.append('.' * board[i] + 'Q' + '.' * (n - board[i] - 1))
                results.append(solution)
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    # bounding here: prune if any conflict
                    continue
                
                # place queen
                board[row] = col
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                backtrack(row + 1)
                
                # remove queen (backtrack)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                board[row] = -1
        
        backtrack(0)
        return results
