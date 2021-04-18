class PriorityQueue:
    def __init__(self):
        self.min_heap = list()
        self.min_heap.append(0)
 
    def is_empty(self):
        if len(self.min_heap) == 1:
            return True
        return False
 
    def put(self, data):
        if (len(data) != 2) and type(data) is tuple:
            return False
        new = len(self.min_heap)
        self.min_heap.append(data)
        while True:
            parent = new // 2
            if new == 1:
                break
            elif self.min_heap[new][0] > self.min_heap[parent][0]:
                break
            else:
                self.min_heap[new], self.min_heap[parent] = self.min_heap[parent], self.min_heap[new]   
                new = parent
           
    def get(self):
        if self.is_empty():
            return None
        current = 1
        returnData = self.min_heap[current][1]
        self.min_heap[current] = self.min_heap[-1]
        del self.min_heap[-1]
        list_len = len(self.min_heap)

        while True:
            left = current * 2
            right = current * 2 + 1
            if left < list_len and right < list_len: # 왼, 오른쪽 둘다 있으면
                if self.min_heap[left][0] < self.min_heap[right][0]: # 왼, 오른쪽 값 비교
                    print("왼", self.min_heap[left][0], self.min_heap[current][0])
                    if self.min_heap[left][0] < self.min_heap[current][0]:
                        self.min_heap[left], self.min_heap[current] = self.min_heap[current], self.min_heap[left]
                        current = left
                    else:
                        break
                else:
                    print("오른", self.min_heap[right][0], self.min_heap[current][0])
                    if self.min_heap[right][0] < self.min_heap[current][0]:
                        self.min_heap[right], self.min_heap[current] = self.min_heap[current], self.min_heap[right]
                        current = right
                    else:
                        break
            elif left < list_len and right >= list_len:
                if self.min_heap[left][0] < self.min_heap[current][0]:
                    self.min_heap[left], self.min_heap[current] = self.min_heap[current], self.min_heap[left]
                    current = left
                else:
                    break
            else:
                break    
        return returnData

 
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.min_heap[1][1]

pq = PriorityQueue()
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))


print(pq.peek())
print(pq.get())
print(pq.min_heap)
print(pq.get())
print(pq.min_heap)
print(pq.get())
print(pq.min_heap)
print(pq.get())
print(pq.min_heap)
print(pq.get())
print(pq.min_heap)
print(pq.get())
print(pq.min_heap)
print(pq.get())
print(pq.min_heap)

