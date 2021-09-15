class newNode:
 
    # Construct to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Function to find sum of all the element
def addBT(root):
    if (root == None):
        return 0
    return (root.key + addBT(root.left) +
                       addBT(root.right))


   