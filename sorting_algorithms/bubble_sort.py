def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"iteration {i}: {arr}")
    return arr


arr = [64, 25, 12, 22, 11]
print(bubble_sort(arr))