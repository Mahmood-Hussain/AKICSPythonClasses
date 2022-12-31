def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        push_idx = i
        for j in range(i - 1, -1, -1):
            if arr[i] < arr[j]:
                push_idx = j  
        arr.insert(push_idx, arr[i])
        arr.pop(i+1)
    return arr

arr = [64, 25, 12, 22, 11]
# print(insertion_sort(arr))

def insertion_sort_2(arr):
    n = len(arr)
    sorted_arr = []
    for i in range(n):
        insert_idx = i
        for j in range(len(sorted_arr) - 1, -1, -1):
            if arr[i] < sorted_arr[j]:
                insert_idx = j
        sorted_arr.insert(insert_idx, arr[i])
    return sorted_arr

arr = [64, 25, 12, 22, 11]
print(insertion_sort_2(arr))  
