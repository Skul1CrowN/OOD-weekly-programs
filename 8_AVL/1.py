class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
    def add(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            current = self.root
            while current:
                if data < current.data:
                    print("L", end="")
                    if not current.left:
                        current.left = Node(data)
                        break
                    current = current.left
                elif data > current.data:
                    print("R", end="")
                    if not current.right:
                        current.right = Node(data)
                        break
                    current = current.right
        print("*")

T = Tree()
inp = list(map(int, input("Enter Input : ").split()))
for e in inp:
    T.add(e)