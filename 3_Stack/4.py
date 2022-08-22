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

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    
    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def size(self):
        return len(self.items)

def infix2postfix(str):
    s = Stack()
    postfix = ''
    operator = '+-*/'
    for i in range(len(str)):
        c = str[i]
        priority = -1 if s.top() == None else operator.find(s.top())//2
        if c in operator:
            while operator.find(c)//2 <= priority:
                postfix += s.pop()
                priority = -1 if s.top() == None else operator.find(s.top())//2
            s.push(c)

        elif c in '(':
            s.push(c)
        
        elif c in ')':
            while s.top() != '(':
                postfix += s.pop()
            s.pop()

        else:
            postfix += c
        
    while not s.isEmpty():
        postfix += s.pop()
        
    return postfix

print(" ***Infix to Postfix***")
token = input("Enter Infix expression : ")
print("PostFix : ")
print(infix2postfix(token))