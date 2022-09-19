class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node('|')
        
    def __str__(self):
        temp = self.head
        strOut = ''
        while (temp):
            strOut += str(temp.data) + ' '
            temp = temp.next
        strOut = strOut[:-1]
        return strOut

    def isEmpty(self):
        return self.head == None
    
    def insert(self, data):
        newNode = Node(data)

        if self.head.data == '|':
            newNode.next = self.head
            self.head = newNode
            return

        temp = self.head
        prev = None
        while temp.data != '|':
            prev = temp
            temp = temp.next
        prev.next = newNode
        newNode.next = temp
    
    def left(self):
        temp = self.head

        if temp.data == '|':
            return
        
        while temp.next.data != '|':
            temp = temp.next
        
        temp.data, temp.next.data = temp.next.data, temp.data

    def right(self):
        temp = self.head

        while temp.data != '|':
            temp = temp.next

        if temp.next is None:
            return
        
        temp.data, temp.next.data = temp.next.data, temp.data
    
    def backspace(self):
        temp = self.head
        prev = None
        
        if temp.data == '|':
            return

        while temp.next.data != '|':
            prev = temp
            temp = temp.next

        prev.next = temp.next
    
    def delete(self):
        temp = self.head

        while temp.data != '|':
            temp = temp.next
        
        if temp.next is None:
            return
        
        temp.next = temp.next.next

inp = list(input("Enter Input : ").split(','))
llist = LinkedList()
for i in inp:
    if i.split(' ')[0] == 'I':
        llist.insert(i.split(' ')[1])
    elif i.split(' ')[0] == 'L':
        llist.left()
    elif i.split(' ')[0] == 'R':
        llist.right()
    elif i.split(' ')[0] == 'B':
        llist.backspace()
    else:
        llist.delete()
print(llist)
        