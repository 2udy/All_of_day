import sys
sys.stdin = open('4864_input.txt')

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
            return 1
    return 0

T = int(input())

for tc in range(1,T+1):
    strs1 = input()
    strs2 = input()
    print(f'#{tc} {KMP_count(strs2,strs1)}')
