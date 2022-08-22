class Queue:
    def __init__(self, data=[]):
        self.items = list(data)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.isEmpty():
            out = self.items[0]
            if self.size() > 1:
                self.items = self.items[1:]
            else:
                self.items = []
            return out
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            return None

    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def size(self):
        return len(self.items)

class Stack:
    def __init__(self,data=[]):
        self.items = data

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    
    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def size(self):
        return len(self.items)
