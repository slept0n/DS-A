
""" usually when we can use a loop we can also use recursion """
""" recursion is mostly a tool that allows us to write cleaner more elegent code """


def factorial(n):
    if n == 1:      # defining our basecase.
        return n    
    else:
        return(n * factorial(n-1))      # this will be called until n = 1


factorial(7)





def fib(n):
    if n <= 3:          # our basecase is defined.
        return(1)
    else:
        return(fib(n-1) + fib(n-2))     # calling the fib function 2 times. known as recursing.
    
print(fib(7))









def binarysearch(data, target, low, high):

    """
    We consider three cases:
• If the target equals data[mid], then we have found the item we are looking for, and the search terminates successfully.
• If target < data[mid], then we recur on the first half of the sequence, that is, on the interval of indices from low to mid − 1.
• If target > data[mid], then we recur on the second half of the sequence, that is, on the interval of indices from mid + 1 to high.
An unsuccessful search occurs if low > high, as the interval [low,high] is empty.
"""

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
            return binarysearch(data, target, mid + 1, high)        # this refers to the right side of the array, since it is sorted.









    
def double_array(array, index=0):
    # Basecase: when the index goes past the end of the array
    if index >= len(array):     # basecase
        return 
    array[index] *= 2           # multiply each element in the array by 2.
    double_array(array, index + 1)      # recurse










