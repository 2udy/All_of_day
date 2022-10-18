import sys
sys.stdin = open('5208_input.txt')

T = int(input())

def count_station(idx, cnt):
    if idx >= N-1:
        chrg.append(cnt)
        return
    k = batteries[idx]
    while k:
        count_station(idx + k, cnt + 1)
        k -= 1

for tc in range(1, T+1):
    batteries = list(map(int, input().split()))
    N = batteries.pop(0)
    chrg = []
    count_station(0, -1)
    print(f'#{tc} {min(chrg)}')