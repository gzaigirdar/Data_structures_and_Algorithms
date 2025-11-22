# %%
'''
Priority Queue: it's specialized verson of queue, data is stored and retrived based on priority of each data element.
- data with highest priority is retrived before data with lower priority.
- data is inserted based on priority of the elements.
- If two elements have same priority then their retrived using FIFO policiy.





'''
# %%
# node for each element, it has data, and priority value
class Node:
    def __init__(self,info,priority):
        self.info = info
        self.priority = priority

# %%
class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    '''
    if queue is not empty, the traverse through the queue and find correct index to add the element.
    if new node has smaller priority then hifghest priority then it will be added to start of the queue 

    '''
    def insert(self,node):
        if len(self.queue) == 0:
            self.queue.append(node)
        else:
            # traverse the queue and find the right index base priority of the new node
            
            for x in range(0,len(self.queue)):
                # if  new the node's priority is bigger or equal to current node, and it is end of the queue then add the new node to end of the queue
                if node.priority >= self.queue[x].priority:
                    # checking to see if the current node is the last node in queue , if so add the new node to end of the queue
                    
                    if x == (len(self.queue)-1):
                        self.queue.insert(x+1,node)
                    else:
                        # continue the loop if it's not end of the queue 
                        continue 
                        
                else:
                    # if current node is not bigger than add the new node in this index and push the current node to next position
                    self.queue.insert(x,node)
                    return True
    # node with highest priority is deleted and removed from the queue
    def delete(self):
        x = self.queue.pop(0)
        return x
    
    def show(self):
        for x in self.queue:
            print(str(x.info)+ "  " + str(x.priority))
    
                 
# %%
pq = PriorityQueue()
pq.insert(Node("Cat",13))
pq.insert(Node("Bat",2))
pq.insert(Node("Tiger",6))
pq.insert(Node("Lion",10))

pq.show()
print('-------------')  
pq.delete()
pq.show()
# %%
