import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charger_points = map(int, input().split())
    charger = [0]*(N+K+1)
    crnt_p = 0
    cnt = []

    for charger_point in charger_points:
        charger[charger_point] = 1

    for charge in charger:
        for i in range(1, K + 1):
            if charger[crnt_p+i]:
                crnt_p += i
                cnt += 1


    print(cnt)
