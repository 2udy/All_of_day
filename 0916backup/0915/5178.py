import sys
sys.stdin = open('5178_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    cnt = 0

    for _ in range(M):
        idx, n = map(int, input().split())
        tree[idx] = n


    for i in range(len(tree)-1,0,-1):
        if (tree[i] == 0) and (i*2+1 < len(tree)):
            tree[i] = tree[i*2] + tree[i*2+1]
        elif (tree[i] == 0):
            tree[i] = tree[i * 2]

    print(f'#{tc} {tree[L]}')
