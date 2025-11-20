


class Node:
    def __init__(self, data):
        self.data = data
        self.prev= None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.prev = self.top
            self.top = new_node
    def pop(self):
        if self.top is None:
            return None
        else:
            d=self.top.data
            self.top = self.top.prev
            return d
    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data
    def is_empty(self):
        return self.top is None
    def display(self):
        l=[]
        current=self.top
        while current is not None:
            l.append(current.data)
            current=current.prev
        print(l[::-1])
obj=Stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.display()
print(obj.pop())

