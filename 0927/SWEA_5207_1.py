import sys
sys.stdin = open('5207_input.txt')

'''

'''


T = int(input())
# dir = 0 1
def check_cross(arr, end, dir):
    if b == arr[len(arr) // 2]:
        return True
    # 키 값이 왼쪽에 있고, 이전에 탐색한 위치가 왼쪽이 아니면
    elif arr[len(arr)//2] >= b and dir != 0:
        arr = arr[:len(arr)//2]
        check_cross(arr, len(arr)//2, 0)

    # 키 값이 오른쪽에 있고, 이전에 탐색한 위치가 오른쪽이 아니면
    elif arr[len(arr)//2] <= b and dir != 1:
        arr = arr[len(arr)//2:]
        check_cross(arr, len(arr), 1)

    # 키값을 찾지 못했거나, 탐색 방향이 잘못 되었다면
    return False

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted(A)

    result = 0

    for b in B:
        if b in A and check_cross(A, len(A), -1):
            result += 1

    print(f'#{tc} {result}')
