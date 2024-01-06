from typing import List
def validSudoku(board : List[List[str]]) -> bool :

    rows = defaultdict(set)
    columns = defaultdict(set)
    squares = defaultdict(set)

    for i in range(9):
        for j in range(9):

            if board[i][j] == ".":
                continue 

            if (board[i][j] in rows[i] or
                board[i][j] in columns[j] or
                board[i][j] in squares[i//3, j//3]):

                return False

            rows[i].add(board[i][j])
            columns[j].add(board[i][j])
            squares[(i//3, j//3)].add(board[i][j])

    return True

def main():
    board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


    print(validSudoku(board))

if __name__ == "__main__":
    main()

