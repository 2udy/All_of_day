import sys
sys.stdin = open('practice2_input.txt')

T = int(input())

for tc in range(1, T+1):
    stack = []
    result = ''
    postfix = input()
    for token in postfix:
        if token not in '*/+-':
            stack.append(int(token))
        else:
            p1 = stack.pop()
            p2 = stack.pop()
            if token == '+':
                stack.append(p2 + p1)
            elif token == '-':
                stack.append(p2 - p1)
            elif token == '*':
                stack.append(p2 * p1)
            elif token == '/':
                stack.append(p2 / p1)
    # 0
    print(stack[-1])