import sys
sys.stdin = open('cake_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cake = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    while True:
        for i in range(N-1):
            for j in range(N-1):
                # (i, j)를 기준으로 자를 때,
                berries = [0, 0, 0, 0] # 각 조각에 포함된  딸기 수를 저장할 리스트
                # 좌상 조각의 딸기 수 저장
                for k in range(i+1):
                    for l in range(j+1):
                        berries[0] += cake[k][l]
                # 좌하 조각의 딸기 수 저장
                for k in range(i+1, N):
                    for l in range(j+1):
                        berries[1] += cake[k][l]
                # 우상 조각의 딸기 수 저장
                for k in range(i+1):
                    for l in range(j+1, N):
                        berries[2] += cake[k][l]
                # 우하 조각의 딸기 수 저장
                for k in range(i+1, N):
                    for l in range(j+1, N):
                        berries[3] += cake[k][l]
                # 네조각의 딸기 수가 모두 같다면 result = 1
                if berries[0] == berries[1] and berries[2] == berries[3] and berries[1] == berries[2]:
                    result = 1
                    break
        # 네조각의 딸기 수가 모두 같게 자를 수 없다면
        break

    print(f'#{tc} {result}')
