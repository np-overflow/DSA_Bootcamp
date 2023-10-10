'''
1.	Working with Linked Lists (Total 8 points)
In this exercise, we will implement a linked list. In this case, you are allowed to copy the example codes into the boxes.

Given: 
class Node:
    def __init__(self, data):
        # Store the value for the node
        self.value = data

a)	Instantiate the node, without a next value. (4 points)
b)	Instantiate a LinkedList(), without a head or a tail. (4 points)

'''

class Node:
    def __init__(self, data):
        self.value = data
    # Leave the node initially without a next value
        self.next = None	

node = Node("Data")
print("The value of the node is:", node.value)
print("The next node of the current node is:", node.next)


class SinglyLinkedList:
    def __init__(self):
    # Set the head and the tail with null values
        self.head = None
        self.tail = None
        self.length = 0

print("The head of the linked list is", SinglyLinkedList().head)
print("The tail of the linked list is", SinglyLinkedList().tail)
