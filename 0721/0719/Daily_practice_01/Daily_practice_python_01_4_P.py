two_seven = []

for i in range(1000):
    if i == 0:
        continue
    elif i%2 == 0:
        two_seven.append(i)
    elif i%7 ==0:
        two_seven.append(i)

print(two_seven)

print(sum(two_seven))