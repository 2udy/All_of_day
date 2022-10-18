import sys
sys.stdin = open('4871_input.txt')

T = int(input())

for tc in range(1,T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G =  map(int, input().split())
    visitied = [0] * (V+1)

    stack = [S]

    while stack:
        v = stack.pop()
        if visitied[v] == 0:
            visitied[v] = 1
            for w in graph[v]:
                if visitied[w] == 0 :
                    stack.append(w)
    result = 1 if visitied[G] == 1 else 0
    print(f'#{tc} {result}')
