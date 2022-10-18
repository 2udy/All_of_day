import sys
sys.stdin = open('1966_input.txt')

T = int(input())

def BubbleSort(a,N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1] , a[j]

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))

    BubbleSort(numbers,N)

    print(f'#{tc}',end=' ')
    print(*numbers)


