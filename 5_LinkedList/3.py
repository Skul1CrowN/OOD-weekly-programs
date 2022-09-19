class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        temp = self.head
        strOut = ''
        while (temp):
            strOut += str(temp.data) + ' '
            temp = temp.next
        strOut = strOut[:-1]
        return strOut

    def reverse(self):
        prev = None
        temp = self.head
        while temp is not None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev

    def isEmpty(self):
        return self.head == None

    def append(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
    
    def insert(self, index, data):
        n = 0
        temp = self.head
        while temp != None:
            temp = temp.next
            n += 1
        if index < 0:
            return False
        elif index == 0:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            return True
        elif index == n:
            self.append(data)
            return True
        else:
            i = 0
            node = self.head
            while i < index-1 and node is not None:
                node = node.next
                i += 1
            if node is None:
                return False
            else:
                newNode = Node(data)
                newNode.next = node.next
                node.next = newNode
                return True

def mergeLinkedList(l1,l2):
    temp = l1.head
    while temp.next is not None:
        temp = temp.next
    temp.next = l2.head

inp1, inp2 = input("Enter Input (L1,L2) : ").split(' ')
inp1 = list(inp1.split('->'))
inp2 = list(inp2.split('->'))
l1 = LinkedList()
l2 = LinkedList()
for i in inp1:
    l1.append(i)
for i in inp2:
    l2.append(i)
print("L1    :",l1)
print("L2    :",l2)
l2.reverse()
mergeLinkedList(l1,l2)
print("Merge :",l1)