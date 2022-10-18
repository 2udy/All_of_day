def dfs(graph, S, visited):
    visited[S] = True
    stack = [S]

    while stack:
        v = stack.pop()
        for i in graph[v]:
            if visited[graph[v]] = True


graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 2. 각 노드가 방문된 정보를 리스트 자료형으로 표현
# 인덱스를 맞춰주기 위해 9개
visited = [False] * 9

# 3. 정의된 DFS 함수 호출
dfs(graph, 1, visited)