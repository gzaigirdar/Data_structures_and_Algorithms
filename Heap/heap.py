# %%
'''
- Heap is specialization of a tree in which the nodes are ordered in a specfic way.
- Min Heap = each parent node has to be smaller or equal to it's children.
- Max heap= each parent node has to be bigger or equal to it's children.

-heap conceaptually a complete binary tree.
(complete binary tree is one which each row must be fully filled before moving on the the next row)
- list is used to implement heap,each nodes children is stored in 2 * i and 2* i + 1 indices.
-indices starts with one so there is dummy element is placed inside index zero.
- root element of a heap is either min or max element.
heap sort:
add the values to heap and then traverse the heap and pop values from root, which will 
give return values in accending order.
'''



# %%
# min heap implementation  

class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0 
    
    # add the new element to end of the list then rearrange the heap based on min/max structure.
    # run time : O(log n)
    def insert(self,value):
        self.heap.append(value)
        self.size += 1
        # pass the index of the last element 
        self.arrange(self.size)
    #run time is O(1)
    def get_min(self):
        
        return self.heap[1]
        
    # arrange function rearranges the heap from bottem to top so it meets the min/max requirment 
    def arrange(self,k):
        # loop is used to swap until heap meets the requirment 
        while k// 2 > 0:
            if self.heap[k] < self.heap[k//2]:
                # swap elements with it's parent if the parent is bigger than the current node
                self.heap[k],self.heap[k//2]= self.heap[k//2],self.heap[k]
            # index changes to parent node after the swap. moving up a tree after a swap
            k //= 2
    # deleting from root
    # remove the root and replace it last element in the heap then rearrange from the top to bottem to meet heap requirement
    # run time: O(log n)
    def delete_at_root(self):
        item = self.heap[1]
        # replaces the root with last element in the heap
        self.heap[1] = self.heap[self.size]
        self.size -=1
        # removes the last element since it's the root now
        self.heap.pop()
        # call sink functiont to rearrange the heap from top to bottem to it meets the min/max requirement
        self.sink(1)
        return item
    # sink functin rearranges the heap from top to bottem from node it takes
    def sink(self,k):
        # loop to traverse down the tree
        while k * 2 <= self.size:
            min_child = self.minChild(k)
            # swap parent with child if parenet is bigger than the min child
            if self.heap[k] > self.heap[min_child]:
                self.heap[k],self.heap[min_child] = self.heap[min_child],self.heap[k]
            k = min_child
    
   def delete_at_location(self, location):
        item = self.heap[location]
        self.heap[location] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()

        if location <= self.size:  
            parent = location // 2
        # if parent is bigger than current then arrange else sink
            if parent > 0 and self.heap[location] < self.heap[parent]:
                self.arrange(location)  
            else:
                self.sink(location)     

        return item

        
    # minchild function finds the child node with minium value
    
    def minChild(self,k):
        # if k*2+1 child doesn't exist then return the k * 2 child
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k*2
        else:
            return k * 2 + 1
    
    def print_items(self):
        print(self.heap)
        

# %%
h1 = Heap()
# heap sort
# run time of heap sort is O(n log n)
for i in (5,6,7,8,9):
    h1.insert(i)

h1.print_items()
#h1.delete_at_root()
h1.delete_at_location(2)
h1.print_items()

# %%
# heap sort
# add values to the heap then pop the values one at at a time
# then the values will be in accending order

heap = Heap()
values = [10,2,50,20,15,5,68,4]

for i in range(len(values)):
    heap.insert(values[i])






# %%
heap.print_items()
# %%
sorted_values = []
for i in range(heap.size):
    sorted_values.append(heap.delete_at_root())
print(sorted_values)
# %%
