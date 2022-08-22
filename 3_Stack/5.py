class Stack:
    def __init__(self,data=[]):
        self.items = data

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

print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split(' ')
m,n = int(m),int(n)
isExist = 0

if s != '0':
    soi = Stack(list(map(int,(s.split(',')))))
else:
    soi = Stack()

if o == 'arrive':
    if soi.size() < m:
        temp = Stack()
        while not soi.isEmpty():
            temp.push(soi.pop())
            if temp.top() == n:
                isExist = 1
                break
        while not temp.isEmpty():
            soi.push(temp.pop())
        if not isExist:
            soi.push(n)
            print('car',n,'arrive! : Add Car', n)
        else:
            print('car',n,'already in soi')
    else:
        print('car', n, 'cannot arrive : Soi Full')
else:
    if soi.isEmpty():
        print('car',n,'cannot depart : Soi Empty')
    else:
        temp = Stack()
        while not soi.isEmpty():
            if soi.top() != n:
                temp.push(soi.pop())
            else:
                isExist = 1
                soi.pop()
        while not temp.isEmpty():
            soi.push(temp.pop())
        if isExist:
            print('car',n,'depart ! : Car',n,'was remove')
        else:
            print('car',n,'cannot depart : Dont Have Car',n)

print(soi.items)