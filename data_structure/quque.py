class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class QueueMgmt:
    def __init__(self):
        self.head = None
        self.rear = None
    
    def is_empty(self):
        if self.head == None:
            return True
        return False

    def insert(self, data):
        if self.is_empty():
            self.head = Node(data)
            self.rear = self.head
        else: 
            temp = self.rear
            self.rear = Node(data, next=temp)
            temp.prev = self.rear

    def pop(self):
        if self.is_empty():
            return None
        else:
            temp = self.head
            self.head = self.head.prev
            nextpop = temp.data
            del temp
            return nextpop

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

queuetest = QueueMgmt()
print(queuetest.is_empty())
print()

for i in range(10):
    queuetest.insert(i)

print(queuetest.is_empty())
print()

for _ in range(10):
    print(queuetest.pop(), end=" ")
print()
print()
print(queuetest.is_empty())
print()
