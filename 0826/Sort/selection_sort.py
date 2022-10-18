arr = [2, 4, 7, 9, 11, 19, 23]

def selection_sort(arr):
    for i in range(len(arr)-1):     # 마지막 요소는 원소가 1개라 정렬할 필요 없음
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort(arr))