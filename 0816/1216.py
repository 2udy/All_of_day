import sys
sys.stdin = open('1216_input.txt')

def palindrome(strings):
    for M in range(99,-1,-1):
        for input_string in strings:
            for i in range(100-M): # 반복 횟수
                for j in range(M//2):
                    if input_string[i+j] == input_string[i-j+M]:
                        if j == M//2-1:
                            return M
                        continue
                    else:
                        break

def horizontal(input_strings) :
    result = []
    for i in range(100):
        result_string = ''
        for j in range(100):
            result_string += input_strings
        result.append(result_string)
    return result

def vertical(input_strings) :
    result = []
    for i in range(100):
        result_string = ''
        for j in range(100):
            result_string += input_strings[j]
        result.append(result_string)
    return result

for tc in range(1,11):
    tc = input()
    for i in range(100):
        input_strings = input()
    ans = palindrome(vertical(input_strings))
    print(f'#{tc} {ans}')