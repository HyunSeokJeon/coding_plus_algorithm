class Node:
    def __init__(self, data, prev=None):
        self.data = data
        self.prev = prev

class stackMgmt:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def insert(self, data):
        if self.is_empty():
            self.head = Node(data)
        else:
            temp = self.head
            self.head = Node(data, prev=temp)

    def pop(self):
        if self.is_empty():
            return None
        else:
            temp = self.head
            temp_data = temp.data
            self.head = temp.prev
            del temp
            return temp_data

stacktest = stackMgmt()

print(stacktest.is_empty())
print()

for n in range(10):
    stacktest.insert(n)

print(stacktest.is_empty())
print()

for _ in range(10):
    print(stacktest.pop(), end=' ')
print()
print()
print(stacktest.is_empty())

