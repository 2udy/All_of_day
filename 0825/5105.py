import sys
sys.stdin = open('5105_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze =[[1]*(N+2)] + [[1]+list(map(int, input()))+[1] for _ in range(N)] +[[1]*(N+2)]
    # maze와 크기가 같은 이차원배열 만들기
    visited = [[0 for _ in range(N+2)] for _ in range(N+2)]
    # delta 상하좌우
    idxs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 시작점찾기
    for i in range(1,N+1):
        for j in range(1, N+1):
            if maze[i][j] == 2:
                start = (i, j)
    Q = [start]
    end = (0,0)

    while Q:
        cp = Q.pop(0)
        for idx in idxs:
            if maze[cp[0]+idx[0]][cp[1]++idx[1]] == 0 and visited[cp[0]+idx[0]][cp[1]+idx[1]] == 0:
                Q.append((cp[0]+idx[0],cp[1]++idx[1]))
                visited[cp[0] + idx[0]][cp[1] + idx[1]] = visited[cp[0]][cp[1]] + 1
            elif maze[cp[0]+idx[0]][cp[1]++idx[1]] == 3:
                visited[cp[0] + idx[0]][cp[1] + idx[1]] = visited[cp[0]][cp[1]] + 1
                end = (cp[0], cp[1])

                break
    print(f'#{tc} {visited[end[0]][end[1]]}')