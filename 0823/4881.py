import sys
sys.stdin = open('4881_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    zero_idxs = [0]*N
    result = 0      # 각 행의 최소값을 저장할


    for i in range(N):
        min_in_line = numbers[i][0]
        for j in range(N):
            if min_in_line > numbers[i][j]:
                min_in_line = numbers[i][j]
        result += min_in_line
        for j in range(N):
            numbers[i][j] -= min_in_line

    for i in range(N):
        for j in range(N):
            if numbers[i][j] == 0:
                zero_idxs[j] += 1

    for idx in zero_idxs:












    print()
