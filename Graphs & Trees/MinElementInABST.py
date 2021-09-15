


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None




# Function to find the minimum element in the given BST.
def minValue(root):
    # Your code here
    
    if root.left == None:
        return root.data
    else:
        return minValue(root.left)