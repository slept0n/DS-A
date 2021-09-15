
# defining a node object. What the nodes attributes are and defining it. so it can exist.
class Node:
    def __init__(self, data=None):
        self.data = data        
        self.next = None    # storing the pointer to the next node. By default if a node is all alone it must have no next pointer.


# a wrapper that wraps over the nodes of what we just created
class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node()

    # the append function will be used to create the first node in the linked list.
    def append(self, data):
        new_node = Node(data)
        cur = self.head     # storing the node we are currently looking at 
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)



my_list = LinkedList()


# adding nodes to the linkedlist.
my_list.append(4)
my_list.append(3)
my_list.append(9)
my_list.append(7)


my_list.display()
