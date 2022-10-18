import sys
sys.stdin = open('4874_input.txt')

T = int(input())

for tc in range(1, T+1):
    stack = []
    result = ''
    postfix = input().split()

    for token in postfix:
        if token == '.':
            if len(stack) == 1:
                result = stack.pop()
                print(f'#{tc} {result}')
            else:
                print(f'#{tc} error')
            break
        # token이 피연산자 일 때
        elif token not in '*/+-':
            stack.append(int(token))

        elif len(stack)< 2 :
            print(f'#{tc} error')
            break
        else:
            p1 = stack.pop()
            p2 = stack.pop()
            if token == '+':
                stack.append(int(p2 + p1))
            elif token == '-':
                stack.append(int(p2 - p1))
            elif token == '*':
                stack.append(int(p2 * p1))
            elif token == '/':
                stack.append(int(p2 / p1))
