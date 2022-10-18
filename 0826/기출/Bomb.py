import sys
sys.stdin = open('Bomb_input.txt')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N, P = map(int, input().split())
    # 인덱싱 에러를 방지하기 위해
    # NxN의 둘레에 0으로 채워진 P 두께의 벽을 쌓음
    bugs = [[0]*(N+2*P)]*P+[[0]*P + list(map(int, input().split())) + [0]*P for _ in range(N)]+[[0]*(N+2*P)]*P

    # pprint(bugs)
    # 첫번째 가로세로 값으로 max 초기화
    max_bug = 0
    for k in range(1, P+1):
        max_bug += bugs[P+k][P]
        max_bug += bugs[P][P+k]
        max_bug += bugs[P-k][P]
        max_bug += bugs[P][P-k]
    max_bug += bugs[P][P]

    for i in range(P, P+N):
        for j in range(P, P+N):
            bug = 0
            # 가로세로 값 탐색
            for k in range(-P, P + 1):
                bug += bugs[i + k][j]
                bug += bugs[i][j + k]
            bug -= bugs[i][j]
            if bug > max_bug:
                max_bug = bug
            # 대각선 값 탐색
            bug = 0
            for k in range(1, P+1):
                bug += bugs[i-k][j-k]
                bug += bugs[i-k][j+k]
                bug += bugs[i+k][j-k]
                bug += bugs[i+k][j+k]
            bug += bugs[i][j]
            if bug > max_bug:
                max_bug = bug
    print(f'#{tc} {max_bug}')
