import sys
sys.stdin = open('5176_input.txt')

T = int(input())

def in_order(i):
    if i:
        in_order(tree[i][0])
        b_tree.append(i)
        in_order(tree[i][1])


for tc in range(1, T+1):
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    b_tree = [0]
    for i in range(1, N+1):
        if i*2<= N:
            tree[i][0] = i*2
        if i * 2+1 <= N:
            tree[i][1] = i*2+1
        tree[i][2] = i
    print(tree)
    in_order(1)
    print(b_tree)
    print(f'#{tc} {b_tree[1]} {b_tree[N//2]}')







# 인덱스를 원소로 갖는 트리를 중위순회


# 중위순회한 순서를 인덱스로 하는 트리 만들기


# V = int(input())
# data = list(map(int, input().split()))
#
#
# ch1 = [0]*(V+1)
# ch2 = [0]*(V+1)
#
# def pre_order(V):
#     if V:
#         pre_order(ch1[V])
#         print(V)
#         pre_order(ch2[V])
#
# for i in range(V-1):
#     p, c = data[i*2], data[i*2+1]
#     if ch1[p] == 0:
#         ch1[p] = c
#     else:
#         ch2[p] = c
#
# pre_order(1)
