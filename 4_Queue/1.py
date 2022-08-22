class Queue:
    def __init__(self) -> None:
        self.list = []
    def enqueue(self, data):
        self.list.append(data)
    def dequeue(self):
        val = self.list[0]
        if len(self.list) > 1:
            self.list = self.list[1:]
        else:
            self.list = []
        return val
    def isEmpty(self):
        return True if len(self.list) == 0 else False
    def size(self):
        return len(self.list)
    def getQueue(self):
        return self.list

def printList(list):
    for i in range(len(list)):
        if i != len(list)-1:
            print(list[i],end=', ')
        else:
            print(list[i],end='')

command = input("Enter Input : ").split(',')
q = Queue()
dequeueList = []
for i in command:
    if i == 'D':
        if q.size() > 0:
            de = q.dequeue()
            dequeueList.append(de)
            print(de ,'<- ',end='')
    else:
        num = i[2]
        q.enqueue(num)

    if q.isEmpty():
        print('Empty',end='')
    else:
        printList(q.getQueue())
    
    print()

if len(dequeueList) == 0:
    print('Empty',end='')
else:
    printList(dequeueList)
print(' : ',end='')
if q.isEmpty():
    print('Empty',end='')
else:
    printList(q.getQueue())
