import sys
sys.stdin = open('1220_input.txt')

def drop (arr) :
    for i in range(100):
        if arr[i] == 1:
            break
        else:
            arr[i] = 0
    for j in range(99, -1, -1):
        if arr[j] == 2:
            break
        else:
            arr[j] = 0

for tc in range(1,11):
    N = int(input())
    magnetics_on_table = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if i < j:
                magnetics_on_table[i][j], magnetics_on_table[j][i] = magnetics_on_table[j][i], magnetics_on_table[i][j]
    cnt = 0

    for magnetics in magnetics_on_table:
        drop(magnetics)
        current_magnetic = 1
        for magnetic in magnetics:
            if current_magnetic != magnetic:
                if magnetic == 2:
                    cnt += 1
                    current_magnetic = 2
                elif magnetic == 1:
                    current_magnetic = 1

    print(f'#{tc} {cnt}')
