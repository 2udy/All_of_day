import sys
sys.stdin = open('1974_input.txt')

T = int(input())

def check_sudoku(board):
    for line in board:
        for i in range(1,10):
            if i not in line:
                return 0
    return 1

def square(board):
    square = []
    for i in range(0,7,3):
        for j in range(0,7,3):
            square_line = []
            for k in range(3):
                for l in range(3):
                    square_line.append(board[i + k][j + l])
            square.append(square_line)
    return square

for tc in range(1,T+1):
    board = [list(map(int, input().split())) for _ in range(9)]

    row = check_sudoku(board)
    squr = check_sudoku(square(board))

    for i in range(9):
        for j in range(9):
            if i < j:
                board[i][j], board[j][i] = board[j][i], board[i][j]

    col = check_sudoku(board)
    if row == 0  or squr == 0 or col == 0:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {1}')




