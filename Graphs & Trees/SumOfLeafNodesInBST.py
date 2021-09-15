#User function Template for python3

##Structure of node
'''
class Node:
    data=0
    left=None
    right=None

'''



def sumOfLeafNodes(root): 
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return root.data
    left = sumOfLeafNodes(root.left)
    right = sumOfLeafNodes(root.right)
    return left+right
    