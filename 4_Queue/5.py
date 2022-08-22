class Queue:
    def __init__(self):
        self.items = []

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

    def reverse(self):
        self.items.reverse()

class Stack:
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    
    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def size(self):
        return len(self.items)

    def reverse(self):
        self.items.reverse()

normal, mirror = input('Enter Input (Normal, Mirror) : ').split(' ')
mirror = mirror[::-1]
mirrorExplosion = 0

mirrorStack = Stack()
mirrorItemQueue = Queue()

for i in mirror:
    if mirrorStack.size() < 2:
        mirrorStack.push(i)
    else:
        mirrorStack.push(i)
        third, second, first = mirrorStack.pop(), mirrorStack.pop(), mirrorStack.pop()
        if not third == second == first:
            mirrorStack.push(first)
            mirrorStack.push(second)
            mirrorStack.push(third)
        else:
            mirrorItemQueue.enqueue(first)
            mirrorExplosion += 1

normalStack = Stack()
fail, normalExplosion, count = 0,0,0

for i in normal:
    if normalStack.size() < 2:
        if normalStack.size() == 1 and i == normalStack.top():
            count = 2
        else:
            count = 0
        normalStack.push(i)
    elif count == 2 and not mirrorItemQueue.isEmpty():
        count = 0
        front = mirrorItemQueue.dequeue()
        normalStack.push(front)
        third, second, first = normalStack.pop(), normalStack.pop(), normalStack.pop()
        if third == second == first:
            fail += 1
        else:
            normalStack.push(first)
            normalStack.push(second)
            normalStack.push(third)
        normalStack.push(i)
    else:
        if i == normalStack.top():
            count = 2
        else:
            count = 0
        normalStack.push(i)
        third, second, first = normalStack.pop(), normalStack.pop(), normalStack.pop()
        if third == second == first:
            normalExplosion += 1
        else:
            normalStack.push(first)
            normalStack.push(second)
            normalStack.push(third)

print('NORMAL : ')
print(normalStack.size())
normalStack.reverse()
if normalStack.isEmpty():
    print('Empty')
else:
    print(''.join(normalStack.items))
print(normalExplosion, 'Explosive(s) ! ! ! (NORMAL)')
if fail > 0:
    print('Failed Interrupted',fail,'Bomb(s)')
print("------------MIRROR------------")
print(": RORRIM")
print(mirrorStack.size())
mirrorStack.reverse()
if mirrorStack.isEmpty():
    print('ytpmE')
else:
    print(''.join(mirrorStack.items))
print('(RORRIM) ! ! ! (s)evisolpxE', mirrorExplosion)