# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    arr_a_index = 0
    arr_b_index = 0
    for i in range(0, len(merged_arr)):
        if arr_a_index == len(arrA):
            merged_arr[i] = arrB[arr_b_index]
            arr_b_index +=1 
        elif arr_b_index == len(arrB):
            merged_arr[i] = arrA[arr_a_index]
            arr_a_index += 1 
        elif arrA[arr_a_index] < arrB[arr_b_index]:
            merged_arr[i] = arrA[arr_a_index]
            arr_a_index += 1        
        elif arrA[arr_a_index] > arrB[arr_b_index]:
            merged_arr[i] = arrB[arr_b_index]
            arr_b_index += 1     
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                arr[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
