class Node:
    def __init__(self,data,left=None,right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

class Stack:
    def __init__(self):
        self.items = []
    
    def append(self,data):
        self.items.append(data)
    
    def peek(self):
        return self.items[-1]
    
    def pop(self):
        return self.items.pop()

class ExpressionTree:
    def __init__(self) -> None:
        self.root = None
    
    def construct(self,postfix):
        if not postfix:
            return
        
        s = Stack()

        for c in postfix:
            if c in '+-*/':
                right = s.pop()
                left = s.pop()

                node = Node(c,left,right)

                s.append(node)

            else:
                s.append(Node(c))

        self.root = s.items[-1]

    def prefix(self,root):
        if root:
            print(root.data,end='')
            self.prefix(root.left)
            self.prefix(root.right)
            
    def infix(self,root):
        if root:
            if root.data in '+-*/':
                print('(',end='')
            self.infix(root.left)
            print(root.data,end='')
            self.infix(root.right)

            if root.data in '+-*/':
                print(')',end='')

    def print(self,root,level=0):
        if root:
            self.print(root.right, level + 1)
            print('     ' * level, root.data)
            self.print(root.left, level + 1)
        
inp = input('Enter Postfix : ')
exptree = ExpressionTree()
exptree.construct(inp)
print('Tree :')
exptree.print(exptree.root)
print('--------------------------------------------------')
print('Infix : ',end='')
exptree.infix(exptree.root)
print()
print('Prefix : ',end='')
exptree.prefix(exptree.root)