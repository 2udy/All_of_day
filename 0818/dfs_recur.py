import sys
from pprint import pprint
sys.stdin = open('input.txt')

def DFS(v):
    # 방문표시 후 출력
    visited[v] = 1
    print(f'방문 정점: {v}, 방문 체크: {visited}')

    for w in range(1,V+1):
        # 인접해있고, 방문하지 않았으면
        if arr[v][w] == 1 and visited[w] == 0:
            # 방문처리를 하기위해 인접 정점을 재귀적으로 호출
            DFS(w)

# V 정점, E 간선
V, E = map(int, input().split())
data = list(map(int, input().split()))

print(data)
# 빈 테이블 만들기
arr = [[0] * (V+1) for _ in range(V+1)]

# 인접행렬 만들기
for i in range(E):
    n1, n2 = data[i*2], data[i*2+1]
    arr[n1][n2] = 1
    arr[n2][n1] = 1

pprint(arr)

# 방문 표시 기록지
visited = [0 for _ in range(V+1)]
DFS(1)

print(visited)