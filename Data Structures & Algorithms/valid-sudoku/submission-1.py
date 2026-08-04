class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(len(board)):
            seenInRow = set()
            for col in range(len(board[row])):
                if board[row][col] == '.':
                    continue
                if board[row][col] not in seenInRow:
                    seenInRow.add(board[row][col])
                else:
                    return False
        for col in range(len(board[0])):
            seenInCol = set()
            for row in range(len(board)):
                if board[row][col] == '.':
                    continue
                if board[row][col] not in seenInCol:
                   seenInCol.add(board[row][col])
                else:
                    return False

        for boxRow in range(len(board) // 3):
            for boxCol in range(len(board[boxRow]) // 3):
                seenInBox = set()
                for row in range(boxRow*3, boxRow*3+3):
                    for col in range(boxCol*3, boxCol*3+3):
                        if board[row][col] == '.':
                            continue
                        if board[row][col] not in seenInBox:
                            seenInBox.add(board[row][col])
                        else:
                            return False
        return True

