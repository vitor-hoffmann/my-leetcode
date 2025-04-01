class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + (j // 3)].add(num)
                else:
                    empties.append((i, j))
        
        def get_candidates(i, j):
            return set('123456789') - rows[i] - cols[j] - boxes[(i // 3) * 3 + (j // 3)]
        
        empties.sort(key=lambda pos: len(get_candidates(pos[0], pos[1])))
        
        def backtrack(index=0):
            if index == len(empties):
                return True  
            i, j = empties[index]
            box_index = (i // 3) * 3 + (j // 3)
            candidates = get_candidates(i, j)
            for num in candidates:
                board[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
                if backtrack(index + 1):
                    return True
                board[i][j] = '.'
                rows[i].remove(num)
                cols[j].remove(num)
                boxes[box_index].remove(num)
            return False

        backtrack()
