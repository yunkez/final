from object.node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        curr = Node(item)
        self.size += 1
        if self.top is None:
            self.top = curr
        else:
            curr.next = self.top
            self.top = curr

    def peek(self):
        return self.top.value

    def pop(self):
        if self.top is None:
            raise Exception("Nothing to pop.")
        curr = self.top
        self.top = self.top.next
        self.size -= 1
        return curr

    def __sizeof__(self):
        return self.size

    def is_empty(self):
        return self.size == 0;