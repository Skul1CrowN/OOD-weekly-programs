class Queue:
    def __init__(self,data=[]):
        self.items = list(data)

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

def encodemsg(msg, qKey):
    for i in range(msg.size()):
        char = msg.dequeue()
        if char >= 'A' and char <= 'Z':
            key = int(qKey.dequeue()) 
            char = chr(((ord(char) + key - 65) % 26) + 65)
        elif char >= 'a' and char <= 'z':
            key = int(qKey.dequeue())
            char = chr(((ord(char) + key - 97) % 26) + 97)
        else:
            continue
        qKey.enqueue(key)
        msg.enqueue(char)
    
    for i in range(qKey.size() - (msg.size() % qKey.size())):
        key = int(qKey.dequeue())
        qKey.enqueue(key)

    print('Encode message is : ',msg.items)

def decodemsg(cipher, qKey):
    for i in range(cipher.size()):
        char = cipher.dequeue()
        if char >= 'A' and char <= 'Z':
            key = int(qKey.dequeue()) 
            char = chr(((ord(char) - key - 65) % 26) + 65)
        elif char >= 'a' and char <= 'z':
            key = int(qKey.dequeue())
            char = chr(((ord(char) - key - 97) % 26) + 97)
        else:
            continue
        qKey.enqueue(key)
        cipher.enqueue(char)
    for i in range(qKey.size() - (cipher.size() % qKey.size())):
        key = int(qKey.dequeue())
        qKey.enqueue(key)

    print('Decode message is : ',cipher.items)

string,number = input('Enter String and Code : ').split(',')
q1 = Queue(string)
q2 = Queue(number)
encodemsg(q1, q2)
decodemsg(q1, q2)