def selection_sort(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"iteration {i}: {arr}")
    return arr


arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))
