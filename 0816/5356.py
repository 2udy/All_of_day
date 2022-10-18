import sys
sys.stdin = open('5356_input.txt')

T = int(input())

for tc in range(1,T+1):
    result_list = []
    result = ''
    for i in range(5):
        input_string = input()
        input_list = []
        for input_char in input_string:
            input_list.append(input_char)

        result_list.append(input_list)

               for k in range(5):
        for l in range(len(result_list[i])):
            result += result_list[l][k]

    print(f'#{tc} {result}')