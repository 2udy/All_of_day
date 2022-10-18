import sys
sys.stdin = open('2001_input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    flies =[list(map(int, input().split())) for _ in range(N)]

    cnts = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for k in range(M):
                for l in range(M):
                    cnt += flies[i+k][j+l]
            cnts.append(cnt)

    result = cnts[0]
    for cnt in cnts:
        if result < cnt:
            result = cnt
    print(f'#{tc} {result}')