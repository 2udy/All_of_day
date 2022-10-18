import sys
sys.stdin = open('4861_input.txt')

T = int(input())

def palindrome(strings,N,M):
    for input_string in strings:
        for i in range(N-M+1):
            for j in range(M//2):
                if input_string[i+j] == input_string[M+i-1-j]:
                    if j == M//2-1:
                        print(f'#{tc} {input_string[-M:]}')
                    continue
                else:
                    break

def origin(input_strings,N) :
    result = []
    for i in range(N):
        result_string = ''
        for j in range(N):
            result_string += input_strings[i*N+j]
        result.append(result_string)
    return result

def reflect(input_strings,N) :
    result = []
    for i in range(N):
        result_string = ''
        for j in range(N):
            result_string += input_strings[i + N * j]
        result.append(result_string)
    return result

for tc in range(1,T+1):
    N, M = map(int,input().split())
    input_strings = ''
    for i in range(N):
        input_strings += input()
    palindrome(origin(input_strings,N),N,M)
    palindrome(reflect(input_strings,N),N,M)




