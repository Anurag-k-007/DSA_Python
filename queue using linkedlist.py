class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def dequeue(self):
        if self.head is None:
            return None
        else:
            d=self.head.data
            self.head=self.head.next
            return d
    def front(self):
        return self.head.data
    def is_empty(self):
        return self.head is None
    def display(self):
        l=[]
        current = self.head
        while current is not None:
            l.append(current.data)
            current = current.next
        print(l)

obj=Queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.display()

