def bubble_sort(arr, N):
    for i in range(N-1,-1,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
    return arr


arr = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(arr)
print(bubble_sort(arr,N))