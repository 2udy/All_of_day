import sys
sys.stdin = open('6485_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    buses = [[],[]]

    for i in range(1,N+1):
        A, B = map(int,input().split())
        buses[0].append(A)
        buses[1].append(B)

    P = int(input())

    stations = [0]*P

    for l in range(P):
        C = input()
        stations[C-1] +=
    for k in range(N):
        for j in range(buses[0][k]-1,buses[1][k]):
            stations[j] += 1

    for l in range(P):
        C = input()

    print(f'#{tc}',end=' ')
    print(*stations)


