board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 0, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

def solve_soduko_board(board):
    find = find_empty_sqaure(board)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid_board(board,i,(row,col)):
            board[row][col] = i

            if solve_soduko_board(board):
                return True

            board[row][col] = 0
    return False




def valid_board(board, number, postion):
    for i in range(len(board[0])):  # check row
        if board[postion[0]][i] == number and postion[1] != i:
            return False
    # check column

    for i in range(len(board)):
        if board[i][postion[1]] == number and postion[0] != i:
            return

    # check 3x3 cubes
    boxX = postion[1] // 3
    boxY = postion[0] // 3

    for i in  range(boxY * 3, boxY * 3 +3):
        for j in range(boxX * 3, boxX * 3 + 3):
            if board[i][j] == number and (i,j) != postion:
                return False
    return True





def print_soduko_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -  ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty_sqaure(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row ,col
    return None


print_soduko_board(board)
solve_soduko_board(board)
print("-------------------------------")
print_soduko_board(board)
