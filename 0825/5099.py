import sys
from collections import deque
sys.stdin = open('5099_input.txt')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    oven = deque()
    result = 0

    pizza_size = list(map(int, input().split()))
    pizza = []

    for i in range(1, M+1):
        pizza.append([i,pizza_size[i-1]])

    for _ in range(N):
        oven.append(pizza.pop(0))

    while oven:
        oven[0][1] = oven[0][1] // 2

        if oven[0][1] != 0:
            oven.append(oven.popleft())
        else:
            oven.pop()
            if len(pizza) != 0:
                oven.append(pizza.pop(0))

    result = oven[0][0]
    print(f'#{tc} {result}')
