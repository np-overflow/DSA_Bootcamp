class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front:", queue.front())  # Output: Front: 1
print("Rear:", queue.rear())    # Output: Rear: 3
print("Size:", queue.size())    # Output: Size: 3

item = queue.dequeue()
print("Dequeued:", item)        # Output: Dequeued: 1

print("Is Empty:", queue.is_empty())  # Output: Is Empty: False
  