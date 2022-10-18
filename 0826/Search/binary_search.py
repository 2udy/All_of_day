arr = [2, 4, 7, 9, 11, 19, 23]

def binary_search(arr, key):
    start = 0
    end = len(arr)
    middle = end//2
    while start <= end : # 양 끝 인덱스가 만날 때 까지 반복
        if key == arr[middle]:
            return middle
        elif key < arr[middle]:
            end = middle - 1
            middle = (start+end)//2
        elif key > arr[middle]:
            start = middle + 1
            middle = (start + end) // 2
    return -1


print(binary_search(arr, 11)) # 4
print(binary_search(arr, 10)) # -1