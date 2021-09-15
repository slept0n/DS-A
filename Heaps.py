

"""a heap is a data struture that deals with "PRIORITY" meaning the root node is always top priority in a queue.
There are min heaps and max heaps. Min heaps is where every descendent aka child of the tree is greater than the root.
a max heap is the opposite meaning the root node is always greater then the rest of its children."""

""" The efficiency of Heaps are 
Insertion: O(log N)
Deletion: O(log N) """


import heapq        # this library helps with creating a Heap data structure.

H = [21,1,45,78,3,5]        
# Covert to a heap
heapq.heapify(H)
print(H)

# Add element
heapq.heappush(H,8)
print(H)

# Remove element from the heap
heapq.heappop(H)



# Replace an element
heapq.heapreplace(H,6)
print(H)










  
# initializing list
li = [5, 7, 9, 1, 3]
  
# using heapify to convert list into heap
heapq.heapify(li)
  
# printing created heap
print ("The created heap is : ",end="")
print (list(li))
  
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)
  
# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))
  
# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))









# Python code to demonstrate working of
# nlargest() and nsmallest()

# importing "heapq" to implement heap queue
import heapq

# initializing list
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(li1)

# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(3, li1))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3, li1))

