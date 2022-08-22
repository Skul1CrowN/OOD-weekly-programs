class Queue:
    def __init__(self, data=[]):
        self.items = list(data)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.isEmpty():
            out = self.items[0]
            if self.size() > 1:
                self.items = self.items[1:]
            else:
                self.items = []
            return out
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            return None

    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def size(self):
        return len(self.items)

id, command = input('Enter Input : ').split('/')
id = list(id.split(','))
command = list(command.split(','))
idList, priorityList = [], []
for i in range(len(id)):
    idList.append(int(id[i].split(' ')[1]))
    priorityList.append(int(id[i].split(' ')[0]))
queue = Queue()
for i in command:
    if i.split(' ')[0] == 'D':
        if queue.isEmpty():
            print('Empty')
        else:
            print(queue.dequeue())
    else:
        temp1, temp2 = Queue(), Queue()
        id = int(i.split(' ')[1])
        priority = priorityList[idList.index(id)]
        if not queue.isEmpty():
            while priority != priorityList[idList.index(queue.peek())]:
                temp1.enqueue(queue.dequeue())
                if queue.isEmpty():
                    break
        if not queue.isEmpty():
            while priority == priorityList[idList.index(queue.peek())]:
                temp2.enqueue(queue.dequeue())
                if queue.isEmpty():
                    break
        temp2.enqueue(id)
        while not temp2.isEmpty():
            temp1.enqueue(temp2.dequeue())
        while not queue.isEmpty():
            temp1.enqueue(queue.dequeue())        
        queue = temp1
        
