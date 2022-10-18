import sys
sys.stdin = open('1224_input.txt')

for tc in range(1, 11):
    N = int(input())
    word = input()
    stack = []
    postfix = ''

# 입력받은 수식을 후위 표기식으로 변경
    for char in word:
        # 연산자를 스택에 저장
        if char in '*+()':
            if len(stack) == 0:
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char in '*':
                # 스택이 비어있지 않고, top이 * 일때 까지
                while stack and stack[-1] in '*':
                    postfix += stack.pop()
                stack.append(char)
            elif char in '+':
                # 스택이 비어있지 않고, top이 ( 일때 까지
                while stack and stack[-1] !='(':
                    postfix += stack.pop()
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] !='(':
                    postfix += stack.pop()
                stack.pop()
        # 피연산자를 후위표기식에 저장
        else:
            postfix += char
    while stack:
        postfix += stack.pop()

    # 후위표기식 연산
    for token in postfix:
        # 피연산자일 경우 스택에 저장
        if token not in '*+':
            stack.append(int(token))
        # 연산자일 경우 연산 결과 스택에 저장
        else:
            p1 = stack.pop()
            p2 = stack.pop()
            if token == '+':
                stack.append(p2 + p1)
            elif token == '*':
                stack.append(p2 * p1)

    print(f'#{tc} {stack[-1]}')