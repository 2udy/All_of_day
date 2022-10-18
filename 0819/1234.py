import sys
sys.stdin = open('1234_input.txt')

for tc in range(1, 11):
    stack = ['A']
    N, chars = map(str, input().split())
    for char in chars:
        if char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()
    result = ''
    for i in range(1,len(stack)):
        result += stack[i]
    print(f'#{tc} {result}')