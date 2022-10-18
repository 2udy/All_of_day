numbers = [1,1,3,3,0,1,1]
result = []

for i, number in enumerate(numbers):
    if i == 0:
        result.append(numbers[i])
    elif numbers[i] == numbers[i-1]:
        continue
    else:
        result.append(numbers[i])


print(result)
