import sys
sys.stdin = open('4873_input.txt')

T = int(input())

for tc in range(1,T+1):
    stack = [0]
    chars = input()
    for char in chars:
        if char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()

    print(f'#{tc} {len(stack)-1}')

