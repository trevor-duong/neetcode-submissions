class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Keep arrays of length 9 to track what numbers we have seen in each row, column, and box
        # Store the nine 3x3 subboxes as a 2d array for ease of calculation
        # To check which row, column, and box we are in requires some checks
        # TO check which row we are in, look at the row index, (similar with column)
        # To check which box we are in, look at both row and column indices (0-3,0-3) -> (0)
        
        rowHistory = [set() for _ in range(9)]
        columnHistory = [set() for _ in range(9)]
        boxHistory = [[set() for _ in range(3)] for _ in range(3)]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == '.':
                    continue
                if num in rowHistory[i]: # check rows
                    print("row fail with num: " + num + " at", i,j)
                    return False
                if num in columnHistory[j]: # check cols
                    print("column fail")
                    return False
                if num in boxHistory[math.floor(i/3)][math.floor(j/3)]:
                    print("box fail")
                    return False
                rowHistory[i].add(num)
                columnHistory[j].add(num)
                boxHistory[math.floor(i/3)][math.floor(j/3)].add(num)
        
        return True
            


