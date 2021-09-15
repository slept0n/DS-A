

"""this function is known as Linear Time: O(n). As the size of the input increases the time increases linearly.
Another way of saying this is : if there are N data elements, how many steps will the algorithm take?"""

given_array = [1, 2, 3, 5, 6]   # as the data increases, we have to keep summing for each element added.

def sum():
  total = 0
  for i in given_array:
    total += i
  return total

print(sum())





"""An algorithm is said to have a constant time when it is not dependent on the input data (n). 
No matter the size of the input data, the running time will always be the same, known as O(1). For example: """

a = 1
b = 2

def BigO1():
    if a > b:
        return True
    else:
        return False


"""An algorithm is said to have a logarithmic time 
complexity when it reduces the size of the input data in each step 
(it doesnt need to look at all values of the input data), Prime example is Binary Search. for example"""
data = [1, 3, 5, 7, 88]

for index in range(0, len(data), 3):            # this is O(log n)
    print(data[index])




"""Algorithms with logarithmic time complexity are commonly found in operations on binary trees or when using binary search. 
Let’s take a look at the example of a binary search, where we need to find the position of an element in a sorted list: """



# this is a (O log N) Algorithm:        Binary search tree is O log n
def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')
    
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(data, 8))




# ****** MORE EXAMPLES *****

"""An algorithm is said to have a linear time complexity when the running 
time increases at most linearly with the size of the input data. 
This is the best possible time complexity when the 
algorithm must examine all values in the input data. For example: """

# O(n)
for value in data:
    print(value)





# a complex example of O(n):       Linear search is O(n). in this example we search every element to find the target.

def linear_search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Value not found in the list')
    
if __name__ == '__main__':
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(linear_search(data, 7))