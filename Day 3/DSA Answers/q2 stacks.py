'''
2.	Working with Stacks (Total 16 points)
In this exercise, we will implement a push operation, using the Node() you have did in Q1. 
On day 2, the stack implemented used elements in a list to push or pop data.
However, this time, we are going to use nodes, instead of elements in a list. 
You can refer to how a Singly Linked List works, for inspiration, from day 1 slides.

Given:
class Stack:
    def __init__(self):
        # Initially there won't be any node at the top of the stack
        self.top = None
        # Initially there will be zero elements in the stack
        self.size = 0

a)	Implement a push function within the stack class. (Start with def will do, no need to copy over the class Stack()). (4 points)
b)	Similar to a), implement a pop function within the stack class. (4 points)

'''


class Node:
  def __init__(self, data):
    self.value = data
    # Leave the node initially without a next value
    self.next = None	


class Stack:
    def __init__(self):
        # Initially there won't be any node at the top of the stack
        self.top = None
        # Initially there will be zero elements in the stack
        self.size = 0

    def push(self, data):
        # Create a node with the data
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        # Set the created node to the top node
        self.top = new_node
        # Increase the size of the stack by one
        self.size += 1

    '''
    #Alternatively, with reference to day 2 slides,
    if you are using self.items = [] as an attribute, you will have "items" to work with.

    def push(self, data):
        new_node = Node(data)
        self.items.append(new_node) 
    '''

    def pop(self):
    # Check if there is a top element
        if self.top is None:
            return None # There is nothing to pop
        else:
            popped_node = self.top
        # Decrement the size of the stack
        self.size -= 1
        # Update the new value for the top node
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data 

    '''
    #Alternatively, with reference to day 2 slides, 
    if you are using self.items = [] as an attribute, you will have "items" to work with.

    def pop(self, data):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"
            # return None # There is nothing to pop
    '''