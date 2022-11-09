import sys
sys.stdin = open('test_input.txt', encoding='utf-8')

def BruteForce(p, t):
    N = len(t)  # 문자열의 길이
    M = len(p)  # 패턴의 길이
    i = 0   # 문자열의 인덱스를 저장할 별수
    j = 0   # 패턴의 인덱스를 저장할 변수
    ans = 0     # 패턴 매칭 횟수를 저장할 변수
    while i < N:    # 문자열을 끝까지 순회하면서
        if t[i] != p[j]:    # 두 문자열이 일치하지 않으면
            i = i - j   # 문자열의 매칭을 시작한 부분으로 돌아가서
            j = -1  # 패턴의 맨 앞으로 돌아가기 위해 -1을 넣고
        i = i + 1   # 방금 비교 시작한 부분 한칸 뒤에서 부터 비교를 시작하고
        j = j + 1   # 패턴의 맨 앞으로 돌아간다 (패턴이 일치할 경우 계속해서 진행될 것이기 때문에)
        if j == M:  # 패턴이 일치할 경우
            ans += 1    # 매칭된 횟수를 1증가 하고
            j = 0   # 패턴의 맨 앞으로 돌아간다.
    return ans

for i in range(10):
    test_case = input()
    P = input()
    T = input()

    result = BruteForce(P, T)
    print(f'#{test_case} {result}')