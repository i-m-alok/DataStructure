# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

class Queue:
    def __init__(self):
        # Code here
        self.instack=Stack()
        self.outstack=Stack()
    def size(self):
         # Code here
        return self.instack.size()

    def enqueue(self,item):
        # Code here
        self.instack.push(item)
    def dequeue(self):
        # Code here
        while self.instack.size():
            data=self.instack.pop()
            self.outstack.push(data)
        value=self.outstack.pop()
        while self.outstack.size():
            data=self.outstack.pop()
            self.instack.push(data)
        return value
