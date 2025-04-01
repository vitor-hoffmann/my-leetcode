class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit == '.':
                    continue 
                
              
                if digit in rows[i]:
                    return False
                rows[i].add(digit)
                
               
                if digit in cols[j]:
                    return False
                cols[j].add(digit)
                
               
                box_index = (i // 3) * 3 + (j // 3)
                if digit in boxes[box_index]:
                    return False
                boxes[box_index].add(digit)
        
        return True
