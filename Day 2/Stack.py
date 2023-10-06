class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top:", stack.top())  # Output: Top: 3
print("Size:", stack.size())  # Output: Size: 3

item = stack.pop()
print("Popped:", item)  # Output: Popped: 3

print("Is Empty:", stack.is_empty())  # Output: Is Empty: False
