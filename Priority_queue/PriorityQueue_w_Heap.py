# %%
class PriorityQueueHeap:
    
    
    def __init__(self):
        self.heap = [()]
        self.size = 0
        
    
    
    
    def insert(self,priority,item):
        # add node to at the end of queue then arrange
        self.heap.append((priority,item))
        self.size += 1
        self.arrange(self.size)
        
    # takes the index of node and rearranges the heap based on it's property from top to bottem  
    def arrange(self,k):
        while k//2> 0:
            # min heap ==> swap parent with child if parent is bigger than child node
            if self.heap[k//2][0] > self.heap[k][0]:
                self.heap[k],self.heap[k//2] = self.heap[k//2],self.heap[k]
            
            k //= 2
                            
    def sink(self, k):
        while k * 2 <= self.size:
            mc = self.min_child(k)
            if self.heap[mc][0] < self.heap[k][0]:
                self.heap[mc],self.heap[k] = self.heap[k],self.heap[mc]
            k = mc
            


    
    # finds the minimum child of an element
    def min_child(self,k):
        # if 2*k+1 chiild doesn't exist return k*2
        if k * 2 +1 > self.size:
            return k * 2
        # return 2k+1 if it's bigger than 2k child
        elif self.heap[k*2][0] < self.heap[k*2+1][0]:
            return k * 2
        else:
           return k * 2 + 1
    
    
    def delete_at_root(self):
        item = self.heap[1][1]
        # replace item with last element in heap then sink to meet the propert
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item
     
        
        
    
    
    # %%
    items = {
        'job1':10,
        'job2':20,
        'job3': 100,
        'job4':5
    }
    h = PriorityQueueHeap()
    for key,value in items.items():
        h.insert(value,key)
    
    

# %%
h.heap
# %%
for i in range(h.size):
    n = h.delete_at_root()
    print(n)
    print(h.heap)

# %%
