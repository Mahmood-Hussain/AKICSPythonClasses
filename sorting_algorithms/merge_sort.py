def merge_sort(arr):
    n = len(arr)
    if n > 1:
        left_sub = arr[:n // 2]
        right_sub = arr[n // 2:]
        merge_sort(left_sub)
        merge_sort(right_sub)

        merger(arr, left_sub, right_sub)


def merger(arr, left_sub, right_sub):
    i = 0
    j = 0
    k = 0
    while i < len(left_sub) and j < len(right_sub):
        if left_sub[i] < right_sub[j]:
            arr[k] = left_sub[i]
            i += 1
        else:
            arr[k] = right_sub[j]
            j += 1
        k += 1

    while i < len(left_sub):
        arr[k] = left_sub[i]
        i += 1
        k += 1

    while j < len(right_sub):
        arr[k] = right_sub[j]
        j += 1
        k += 1


arr = [64, 25, 12, 22, 11]
merge_sort(arr)
print(arr)