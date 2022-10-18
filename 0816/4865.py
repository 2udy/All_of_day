import sys
sys.stdin = open('4865_input.txt')

T = int(input())

for tc in range(1,T+1):
    strs1 = input()
    strs2 = input()
    cnt_list = []

    for str1 in strs1:
        cnt = 0
        for str2 in strs2:
            if str1 == str2:
               cnt += 1
        cnt_list.append(cnt)

    max_cnt = cnt_list[0]
    for cnt in cnt_list:
        if cnt >= max_cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')

