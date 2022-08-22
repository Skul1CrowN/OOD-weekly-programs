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

def match(open, close):
    return (open == '(' and close == ')') or (open == '{' and close == '}') or (open == '[' and close == ']')

def parenthesisMatch(str):
    s, i, error = Stack(), 0, 0

    while i < len(str) and error == 0:
        c = str[i]
        if c in '{[(':
            s.push(c)
        else:
            if c in '}])':
                if s.size() > 0:
                    if not match(s.pop(), c):
                        error = 1
                else:
                    error = 2
        i += 1

    if s.size() > 0 and error == 0:
        error = 3

    return error,c,i,s

str = input("Enter expresion : ")
err,c,i,s = parenthesisMatch(str)
if err == 1:
    print(str, 'Unmatch open-close',end='  ')
elif err == 2:
    print(str, 'close paren excess',end='  ')
elif err == 3:
    print(str, 'open paren excess',end='   ')
    print(s.size(), ': ', end='')
    for ele in s.items:
        print(ele,sep=' ',end = '')
else:
    print(str,'MATCH')