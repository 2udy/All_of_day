import sys
sys.stdin = open('3143_input.txt')

T = int(input())

def pre_process(P):
    lps = [0]* len(P)
    j = 0
    for i in range(1,len(P)):
        if P[i] == P[j]:
            lps[i] = j + 1
            j += 1
        else:
            j = 0
            if P[i] == P[j]:
                lps[i] = j + 1
                j += 1
    return lps

def KMP_count(T,P):
    lps = pre_process(P)
    i = 0
    j = 0
    cnt = 0

    while i < len(T):
        if T[i] == P[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == len(P):
            cnt += 1
            j = 0
    return cnt


for tc in range(1,T+1):
    T, P = map(str,input().split())
    print(f'#{tc} {len(T) - (len(P)-1)*KMP_count(T,P)}')
