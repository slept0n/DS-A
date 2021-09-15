
"""for a binary search to work, the array MUST be sorted"""
# binary search a sorted array

def search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2 # make sure to round it down
        if arr[mid] == target:
	        return mid
        elif target < arr[mid]:
	        right = mid - 1
        else:
            left = mid + 1
    return -1



arr1 = [-2, 3, 4, 7, 8, 9, 11, 13]   # for a binary search to work, the array MUST be sorted already
assert search(arr1, 11) == 6
assert search(arr1, 13) == 7
assert search(arr1, -2) == 0
assert search(arr1, 8) == 4
assert search(arr1, 6) == -1
assert search(arr1, 14) == -1
assert search(arr1, -4) == -1

arr2 = [3]
assert search(arr2, 6) == -1
assert search(arr2, 2) == -1
assert search(arr2, 3) == 0

print("If you didn't get an assertion error, this program has run successfully.")







# Another good example that uses recursion:







def binarysearch(data, target, low, high):


    """
    We consider three cases:
• If the target equals data[mid], then we have found the item we are looking for, and the search terminates successfully.
• If target < data[mid], then we recur on the first half of the sequence, that is, on the interval of indices from low to mid − 1.
• If target > data[mid], then we recur on the second half of the sequence, that is, on the interval of indices from mid + 1 to high.
An unsuccessful search occurs if low > high, as the interval [low,high] is empty.
"""
    low = 0
    high = len(data)-1
    
    if low > high:
        return False        # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:     # found a match
            return True
        elif target < data[mid]:
            return binarysearch(data, target, low, mid-1)
        else:
            # recur on the portion right of the middle
            return binarysearch(data, target, mid + 1, high)        # this refers to the right side of the array