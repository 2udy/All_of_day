import sys
sys.stdin = open('4871_input.txt')

T = int(input())

def DFS(v):

    stack = [v]
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1

            for w in range(1, V+1):
                if G[v][w] == 1 and visited[w] == 0:
                    stack.append(w)

for tc in range(1,T+1):
    V, E = map(int, input().split())

    G = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        G[n1][n2] = 1
        G[n2][n1] = 1
    ps, pe = map(int, input().split())

    visited = [0 for _ in range(V + 1)]

    DFS(ps)

    if visited[pe] == 1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
