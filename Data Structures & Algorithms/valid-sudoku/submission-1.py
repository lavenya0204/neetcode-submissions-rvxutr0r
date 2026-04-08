class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        box=defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                else:
                    n=board[r][c]
                    if (n in col[c] or
                    n in row[r] or 
                    n in box[r//3,c//3]):
                     return False
                    else:
                        col[c].add(n)
                        row[r].add(n)
                        box[r//3,c//3].add(n)
        return True 
