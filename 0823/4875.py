import sys
sys.stdin = open('4875_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    # 상하좌우
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 시작점과 끝점 좌표 찾기
    for i in range(N):
        if miro[0][i] == 3:
            end_x = 0
            end_y = i
        for j in range(N):
            if miro[i][j] == 2:
                start_x = i
                start_y = j
    # 갈림길 위치 저장할 스택
    stack = [[0, end_y]]    # 끝점을 맨 처음
    # 갈림길 갯수 저장할 변수
    cnt = 0
    while len(stack) != 0 and cnt != 0:
        current_point = miro[end_x][end_y]
        if current_point == miro[start_x][start_y]:
            result = 1

        # if current_point
