class Stack:
    def __init__(self):
        self.items = []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    def isEmpty(self):
        return True if len(self.items) == 0 else False
    def size(self):
        return len(self.items)
    
print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter data to stack : ").split()]
s = Stack()
for e in ls:
    s.push(e)
print(s.size(),"Data in stack : ",s.items)
while not s.isEmpty():
    s.pop()
print(s.size(),"Data in stack : ",s.items)

