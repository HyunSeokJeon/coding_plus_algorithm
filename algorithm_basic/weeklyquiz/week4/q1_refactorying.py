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
        heap = self.min_heap
        current_num = len(heap)
        heap.append(data)
        while True:
            parent_num = current_num // 2
            if current_num == 1:
                break
            elif heap[current_num][0] > heap[parent_num][0]:
                break
            else:
                heap[current_num], heap[parent_num] = heap[parent_num], heap[current_num]   
                current_num = parent_num
           
    def get(self):
        if self.is_empty():
            return None
        # 가독성을 위한 변수 선언
        heap = self.min_heap
        current_num = 1
        # 리턴값 저장, 마지막에 들어온 값을 힙의 root에 복사 후, 삭제
        return_data = heap[current_num][1]
        heap[current_num] = heap[-1]
        del heap[-1]
        # 정렬을 위한 heap크기
        heap_len = len(heap)
        # 중복함수 격리
        def child_check(self, direction):
            D = direction
            current_num = D // 2
            if heap[D][0] < heap[current_num][0]:
                heap[D], heap[current_num] = heap[current_num], heap[D]
                return D
            else:
                self.flag = True
        # 정렬
        while True:
            L = current_num * 2
            R = current_num * 2 + 1
            self.flag = False
            if L < heap_len and R < heap_len:
                if heap[L][0] < heap[R][0]:
                    current_num = child_check(self, L)
                else:
                    current_num = child_check(self,R)
            elif L < heap_len and R >= heap_len:
                current_num = child_check(self,L)
            else:
                break   

            if self.flag:
                break
            
        return return_data
    
 
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

