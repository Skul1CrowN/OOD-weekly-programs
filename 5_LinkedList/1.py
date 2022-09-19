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
            strOut += str(temp.data) + '->'
            temp = temp.next
        strOut = strOut[:-2]
        return strOut

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
        

listCommand = input('Enter Input : ').split(',')
linkedList = LinkedList()
for i in listCommand:
    if ':' in i:
        if not linkedList.insert(int(i.split(':')[0]), int(i.split(':')[1])):
            print('Data cannot be added')
        else:
            print('index =', i.split(':')[0].lstrip(), 'and data =', i.split(':')[1])
    else:
        if not len(i) == 0:
            elements = i.split(' ')
            for j in elements:
                linkedList.append(int(j))
    if linkedList.isEmpty():
        print('List is empty')
    else:
        print('link list :',linkedList)
