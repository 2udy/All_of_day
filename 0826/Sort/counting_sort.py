def counting_sort(arr, max_num):
    count_arr = [0]*(max_num+1)
    # count_arr에 입력
    for a in arr:
        count_arr[a] += 1    # [1, 3, 1, 1, 2]
    # count_arr 갱신
    for i in range(1, max_num+1):
        count_arr[i] += count_arr[i-1]  # [1, 4, 5, 6, 8]
    # result 생성
    result = [0]*len(arr)
    # result에  input을 count_arr의 인덱스로 하는 input 추가
    for b in arr:
        count_arr[b] -= 1
        result[count_arr[b]] = b
    return result

numbers = [0, 4, 1, 3, 1, 2, 4, 1]

max_num = numbers[0]

for number in numbers:
    if number > max_num:
        max_num = number

print(counting_sort(numbers, max_num))