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
            strOut += str(temp.data) + ' -> '
            temp = temp.next
        strOut = strOut[:-4]
        return strOut

    def printWithoutArrow(self):
        temp = self.head
        strOut = ''
        while (temp):
            strOut += str(temp.data) + ' '
            temp = temp.next
        strOut = strOut[:-1]
        return strOut

    def isEmpty(self):
        return self.head == None
    
    def peekFront(self):
        return self.head.data
    
    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = Node(data)
    
    def addHead(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def insertSort(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        
        temp = self.head
        if data < temp.data:
            self.addHead(data)
            return

        while temp.next is not None:
            if data < temp.next.data:
                break
            temp = temp.next
        
        if temp.next is None:
            self.append(data)
            return
        
        newNode = Node(data)
        newNode.next = temp.next
        temp.next = newNode
    
    def removeFront(self):
        temp = self.head
        if temp is None:
            return
        self.head = temp.next

        return temp.data
    
    def removeBack(self):
        temp = self.head
        if temp is None:
            return

        if temp.next is None:
            value = temp.data
            self.head = None
            return value
        
        prev = None
        while temp.next is not None:
            prev = temp
            temp = temp.next

        value = temp.data
        prev.next = None
        return value
    
    def size(self):
        n = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            n += 1
        return n

def radixSort(llist):
    modder = 10
    divider = 1
    num_llist = [LinkedList() for i in range(10)]
    round = 1
    temp = llist.head
    print_llist = llist
    num = 0
    while 1:
        print('------------------------------------------------------------')
        print('Round :', round)
        temp = llist.head
        while temp is not None:
            if temp.data >= 0:
                num = (temp.data % modder) // divider
            else:
                num = (-temp.data % modder) // divider

            num_llist[num].insertSort(temp.data)
            temp = temp.next

        for i in range(len(num_llist)):
            print(i,":",num_llist[i].printWithoutArrow())
        
        if num_llist[0].size() == llist.size():
            llist = num_llist[0]
            print('------------------------------------------------------------')
            print(round-1,'Time(s)')
            print("Before Radix Sort :",print_llist)
            print("After  Radix Sort :",llist)
            return

        llist_temp = LinkedList()
        for i in range(len(num_llist)):
            neg_llist,pos_llist = LinkedList(),LinkedList()
            while not num_llist[i].isEmpty():
                if num_llist[i].peekFront() >= 0:
                    pos_llist.append(num_llist[i].removeFront())
                else:
                    neg_llist.append(num_llist[i].removeFront())
                
            while not neg_llist.isEmpty():
                llist_temp.addHead(neg_llist.removeBack())
            while not pos_llist.isEmpty():
                llist_temp.append(pos_llist.removeFront())
        
        modder *= 10
        divider *= 10
        round += 1
        llist = llist_temp
    
inp = list(map(int, input("Enter Input : ").split()))
llist = LinkedList()
for i in inp:
    llist.append(i)
radixSort(llist)