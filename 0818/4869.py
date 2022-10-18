import sys
sys.stdin = open('4869_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    if N%20 == 0:
        result = 2**(N//10-1)
    else:
        n = N//20
        result = 0
        for i in range(n+1):
            result += 4**i

    print(f'#{tc} {result}')