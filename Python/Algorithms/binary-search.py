def rec_binary_search(array, element, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if element == array[mid]:
        return mid
    
    elif element < array[mid]:
        return rec_binary_search(array, element, start, mid-1)
    
    else:
        return rec_binary_search(array, element, mid+1, end)

element = 18
array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]

print(f"Searching for {element}")
print(f"Index of {element}: {rec_binary_search(array, element, 0, len(array))}")