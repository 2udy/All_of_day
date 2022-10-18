import sys
sys.stdin = open('4866_input.txt')

T = int(input())

def pair_check(parenthesises):
    stack = []
    for parenthesis in parenthesises:
        if parenthesis == '(':
            stack.append(parenthesis)
        elif parenthesis == '{':
            stack.append(parenthesis)
        elif parenthesis == '[':
            stack.append(parenthesis)

        else:
            if parenthesis == ')':
                if len(stack) == 0:
                    return 0
                elif stack[-1] == '(':
                    stack.pop()
                else:
                    return 0
            elif parenthesis == '}':
                if len(stack) == 0:
                    return -1
                elif stack[-1] == '{':
                    stack.pop()
                else:
                    return 0
            elif parenthesis == ']':
                if len(stack) == 0:
                    return -1
                elif stack[-1] == '[':
                    stack.pop()
                else:
                    return 0
    if stack == []:
        return 1
    else:
        return 0

for tc in range(1,T+1):
    parenthesises = input()
    print(f'#{tc} {pair_check(parenthesises)}')


