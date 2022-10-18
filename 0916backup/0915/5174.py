import sys
sys.stdin = open('5174_input.txt')

T = int(input())


for tc in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    ch = [[0]*(E+2), [0]*(E+2)]
    cnt = 0
    Q = []
    for i in range(E):
        p, c = data[i*2], data[i*2+1]
        if ch[0][p] == 0:
            ch[0][p] = c
        else:
            ch[1][p] = c

    if ch[0][N] != 0 and ch[1][N] != 0:
        cnt += 1
        Q.append(ch[0][N])
        Q.append(ch[1][N])
    elif ch[0][N] != 0 and ch[1][N] == 0:
        cnt += 1
        Q.append(ch[0][N])
    else:
        cnt += 1
    while Q:
        N = Q.pop(0)
        cnt +=1
        if ch[0][N] != 0 and ch[1][N] != 0:
            Q.append(ch[0][N])
            Q.append(ch[1][N])
        elif ch[0][N] != 0 and ch[1][N] == 0:
            Q.append(ch[0][N])

    print(f'#{tc} {cnt}')