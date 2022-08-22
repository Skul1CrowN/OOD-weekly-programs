class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,data):
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

inQueue, q1, q2 = Queue(), Queue(), Queue()
str = input("Enter people : ")
count, q1Minute, q2Minute = 1, 0, 0

for i in str:
    inQueue.enqueue(i)

while not inQueue.isEmpty():
    if q1Minute != None:
        if q1Minute % 3 == 0 and q1Minute != 0:
            q1.dequeue()
    
    if q2Minute != None:
        if q2Minute % 2 == 0 and q2Minute != 0:
            q2.dequeue()
    
    if q1.size() < 5:
        q1.enqueue(inQueue.dequeue())
    else:
        q2.enqueue(inQueue.dequeue())

    print(count,inQueue.items,q1.items,q2.items)

    count += 1
    q1Minute += 1
    q2Minute += 1

    if q1.isEmpty():
        q1Minute = 0
    if q2.isEmpty():
        q2Minute = 0