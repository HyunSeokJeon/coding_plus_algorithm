class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class LinkedListMgmt:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current_node = self.head
            if current_node.next != None:
                current_node = current_node.next
            current_node.next = Node(data)

    def search(self, data):
        if self.head == None:
            return None
        else:
            current_node = self.head
            if current_node:
                if current_node.data == data:
                    return True
                current_node = current_node.next
            return False
    
    def insert(self, data, base):
        if not self.search(base):
            return "is empty or not found base"
        else:
            current_node = self.head
            if current_node.next.data

