class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        newNode = Node(item)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
            return

        newNode.previous = self.tail
        self.tail.next = newNode
        self.tail = newNode
        

    def addHead(self, item):
        newNode = Node(item)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
            return
        
        newNode.next = self.head
        self.head.previous = newNode
        self.head = newNode

    def insert(self, pos, item):
        newNode = Node(item)
        if pos < 0:
            temp = self.tail
            for i in range(-pos-1):
                if temp is None:
                    break
                temp = temp.previous
            
            if temp is None or temp.previous is None:
                self.addHead(item)
                return

            newNode.next = temp
            newNode.previous = temp.previous
            temp.previous = newNode
            newNode.previous.next = newNode
        elif pos == 0:
            self.addHead(item)
            return
        else:
            temp = self.head
            for i in range(pos-1):
                if temp is None:
                    break
                temp = temp.next
            
            if temp is None or temp.next is None:
                self.append(item)
                return
            
            newNode.previous = temp
            newNode.next = temp.next
            temp.previous = newNode
            newNode.next.previous = newNode 
            
    def search(self, item):
        temp = self.head
        while temp is not None:
            if temp.value == item:
                return 'Found'
            temp = temp.next
        
        return 'Not Found'

    def index(self, item):
        i,n = -1,0
        temp = self.head
        while temp is not None:
            if temp.value == item:
                i = n
                break
            n += 1
            temp = temp.next
        return i

    def size(self):
        n = 0
        temp = self.head
        while temp is not None:
            n += 1
            temp = temp.next
        return n

    def pop(self, pos):
        if pos < 0:
            return 'Out of Range'

        elif pos == 0 and self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
            return 'Success'
        else:
            temp = self.head
            for i in range(pos-1):
                if temp is not None:
                    temp = temp.next

            if temp is not None and temp.next is not None:
                temp.next = temp.next.next
                if temp.next.next is not None:
                    temp.next.next.previous = temp.next
            
                return 'Success'
            else:
                return 'Out of Range'

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())