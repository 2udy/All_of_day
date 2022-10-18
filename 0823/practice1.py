import sys
sys.stdin = open('practice1_input.txt')

T = int(input())

for tc in range(1, T+1):
    stack = []
    result = ''
    word = input()

    for char in word:
        if char in '*+-/()':
            if len(stack) == 0:
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char in '*/':
                    # 스택이 비어있지 않고,
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(char)
            elif char in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(char)
            elif char ==')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                # ( 이면 stack에서 꺼내기만 하고 result에 넣지 않는다.
                stack.pop()
        else:
            result += char
    while stack:
        result += stack.pop()
    print(result)