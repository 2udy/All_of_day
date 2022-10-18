import sys
sys.stdin = open('1979_input.txt')

T = int(input())

def count_len(board,N,M):
    lengthes = []
    cnt = 0

    for line in board:
        length = 0
        for i in line:
            if i == 1:
                length += 1
            else:
                if length != 0 :
                    lengthes.append(length)
                length = 0
        if length != 0:
            lengthes.append(length)
    for j in lengthes:
        if j == M:
            cnt += 1
    return cnt

for tc in range(1,T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    a = count_len(board, N, M)
    for i in range(N):
        for j in range(N):
            if i<j:
                board[i][j], board[j][i] = board[j][i], board[i][j]
    b = count_len(board, N, M)
    print(f'#{tc} {a+b}')