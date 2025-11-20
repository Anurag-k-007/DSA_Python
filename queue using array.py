class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)  # Add item at the end (rear)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)  # Remove and return item from the front

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]  # Returns the front item without removing
