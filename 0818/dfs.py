import sys
from pprint import pprint
sys.stdin = open('input.txt')

def DFS(v):
    #stack에 시작 지점을 넣고 시작
    stack = [v]

    # stack이 빌 때까지 반복
    # (stack이 공백이라는 이유는 모든 그래프 탐색 완료라는 뜻)
    while stack:
        # stack의 가장 위에서 값을 꺼내어(top) 정점으로 두고
        v = stack.pop()
        # 정점 v가 아직 방문하지않은(visited에서 0인지) 정점이라면
        if visited[v] == 0:
            # 일단 방문 처리
            visited[v] = 1
            # 해당 방문 정점을 출력
            print(f'방문 정점: {v}, 방문 체크: {visited}')

            # 반복을 돌며 다음 이동할 곳을 찾는다
            # for w in range(V, 0, -1):     순회 순서 변경
            for w in range(1, V+1):
                # 1. 해당 정점(V)의 인접정점(w)이고
                # 2. 이 인접 정점에 아직 방문하지 않았다면
                if arr[v][w] == 1 and visited[w] == 0:
                    # 인점 정점을 방문하기 위해 stack에 추가
                    stack.append(w)

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