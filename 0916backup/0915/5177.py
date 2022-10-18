import sys
sys.stdin = open('5177_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    data = list(map(int, input().split()))
    ans = 0

    for i in range(1, N+1):
        tree[i] = data[i-1]
        while tree[i//2] > tree[i]:
            tree[i//2], tree[i] = tree[i], tree[i//2]
            i = i//2

    while N != 0:
        ans += tree[N//2]
        N = N//2

    print(f'#{tc} {ans}')
