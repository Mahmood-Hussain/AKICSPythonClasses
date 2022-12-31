def bs(arr, low_idx, high_idx, target):
    if low_idx > high_idx:
        return -1
    else:
        mid_idx = (low_idx + high_idx) // 2
        if target == arr[mid_idx]:
            return mid_idx
        elif target < arr[mid_idx]:
            low_idx = low_idx
            high_idx = mid_idx - 1
            return bs(arr, low_idx, high_idx, target)
        elif target > arr[mid_idx]:
            low_idx = mid_idx + 1
            high_idx = high_idx
            return bs(arr, low_idx, high_idx, target)

# arr = [1, 2, 4, 6, 10, 13, 17, 21, 34, 56, 98]
arr = [3]
low = 0
high = len(arr) - 1
target = 1
print(bs(arr, low, high, target))
