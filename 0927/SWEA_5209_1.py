import sys
sys.stdin = open('5209_input.txt')

'''
[최소 생산 비용]
1. 재귀 종료 조건: 제품 번호 == N
---> 파라미터 (제품번호)    
2. pruning: 현재 비용 > 최소비용 : 유망하지 않음
---> 파라미터(현재비용, 최소비용)

3. 재귀함수
visited 리스트 필요
해당 공장을 방문 한 적 없을 때
재귀함수로 비용 탐색
돌아와서 다시 방문 표시 지우기
'''

def lowest_cost(num, crnt_cost, min_cost):
    # 재귀 종료 조건: num(제품 번호) == N(제품 종류 수)
    if num == N:
        return min(crnt_cost, min_cost)
    # pruning: 현재까지의 비용 > 최소 비용 이면 유망하지 않다.
    elif crnt_cost > min_cost:
        return min_cost
    # N개의 공장을 순회하며 최소값을 찾는다.
    for i in range(0, N):
        # i번째 공장에 방문한 적이 없다면 방문한다.
        if not visited[i]:
            # 방문표시하고
            visited[i] = 1
            # 다음 번호의 제품(num+1)을 생산할 공장을 찾는다.
            min_cost = lowest_cost(num + 1, crnt_cost + costs[num][i], min_cost)
            # 다음 방문을 위해 방문표시를 지운다.
            visited[i] = 0
    # 최소값을 리턴한다.
    return min_cost

T = int(input())

for tc in range(1, T + 1):
    # 제품의 종류 수, 공장 수 입력
    N = int(input())
    # 비용 입력
    costs = [list(map(int, input().split())) for _ in range(N)]
    # 방문표시 리스트 생성
    visited = [0] * N
    # 최소비용 탐색
    result = lowest_cost(0, 0, sum(sum(costs, [])))
    # 정답 출력
    print(f'#{tc} {result}')