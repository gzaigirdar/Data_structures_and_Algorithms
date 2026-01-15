# %%
'''
  ---------Useful Hash Table definitions ----------------
- Hash table is data structure where elements are accessed by keyword rather
than index. 
- Hash table usesed hashing function to find index where the key and value 
are stored.
- Hash function converts the key to integer values, which is used to convert the key 
to  integer. Perfect hashing function is one that gives unique index to each key.
- Slot(bucket): is a postion in hash table that can store an element.
- collision: when two key map to same index is called collision.
- Multiplier: multiplying each index value for each character interget hash function helps prevent collision. Usually multipler grows with each chracter in the string.

- Modulo operator: the modulo operator % returns the remainder after dividing one number by another (for example, 7 % 5 is 2). 
The result is always in the range 0 to divisor − 1, so it gives the value in range. Used to find indices for hash table.
- count: number of slots that already in use.
- size: number of total slots available.
- Load Factor: dividing number of used slots by the total number of slots available in the table,it is ratio between count and size.
Load factor = n/k (n=count,k=slots). It is used to expand the size of the hash table.


'''


# %%
# python ord() function takes a chracter and returns the integer value(ordinal Number)that is assosiated with unicode encoding system
print(ord('a'))
print(ord('a'))
# getting integer value for a string by summing of their ordinal number for each character
print(sum(map(ord,'ab')))
# %%
class HashItem:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        
# %%
class HashTable:
    def __init__(self):
        # size is total number of slots in the table(used or unused)
        self.size = 265
        # count is number of slots that are already in use
        self.count = 0
        # creates empty slots for up to size - 1
        self.slots = [None for i in range(self.size)]
        # max load factor; if max load factor is reached then incrase the size of the hash table
        self.MAXLOADFACTOR = 0.65
        
    # _ indicates private function in python that can only be called by the class itself.
    def _hash(self,key):
        # multiplier that increases by each character
        multi = 1
        hash_value = 0
        for char in key:
            hash_value += multi * ord(char)
            # increase the multiplier by one
            multi += 1
        # return the index using modulus operator 
        # will return index between 0 to self.size-1
        return hash_value % self.size 
    
    
    # storing element in hash table
    # if item already exits then update else find a new slot to add and then update count
    def get(self,key):
        hash = self._hash(key)
        while self.slots[hash] != None:
            if self.slots[hash].key == key:
                return self.slots[hash].value
            hash = (hash+1) % self.size
        return None
    def put(self,key,value):
        item = HashItem(key,value)
        hash_index = self._hash(key)
        # keep looping the table unitl empty slot is found
        while self.slots[hash_index] != None:
            # break if key already exists; in that case update the value
            if self.slots[hash_index].key == key:
                break       
            # linear probing by increseing hash_index to find empty slot
            hash_index = (hash_index+1) % self.size
        
        if self.slots[hash_index] == None:
            self.count += 1
        self.slots[hash_index] = item 
        self.check_growth()
    
    # checks to see if load factor if bigger than max load factor, if so then it expands the hash table by calling growth function
    def check_growth(self):
        loadfactor = self.count/self.size
        
        if loadfactor> self.MAXLOADFACTOR:
            print("Load factor before growing hash table:",self.count/self.size)
            self.growth()
            print("Load factor after growing hash table:",self.count/self.size)
        
    def get_growth(self):
        return self.count/self.size
    def _put_no_growth(self, key, value):
        item = HashItem(key, value)
        hash_index = self._hash(key)

        while self.slots[hash_index] is not None:
            if self.slots[hash_index].key == key:
                break     
            hash_index = (hash_index + 1) % self.size

        self.slots[hash_index] = item
        self.count += 1

    def growth(self):
        New_Hash_Table = HashTable()
        # increases the hashtable by factor of 2
        New_Hash_Table.size = 2 * self.size
        New_Hash_Table.slots = [None for i in range(New_Hash_Table.size)]
        
        # update the new hashtable with  existing slots from old hash table
        
        for i in range(self.size):
            
            if self.slots[i] != None:
                New_Hash_Table._put_no_growth(self.slots[i].key,self.slots[i].value)
        
        self.size = New_Hash_Table.size
        self.slots = New_Hash_Table.slots
        self.count = New_Hash_Table.count
    def __setitem__(self,key,value):
        return self.put(key,value)
    def __getitem__(self,key):
        return self.get(key)
# %%
ht = HashTable()    

# %%

ht.put("england","London")
ht.put("Spain","Madrid")    
ht.put('Bangladesh',"Dhaka")
ht.put('Australia',"Sydney")


# %%
ht['Mexico'] = 'Mexico City'
ht.get_growth()
# %%
ht.get('england')
# %%
for key in ('england','Spain','Bangladesh','Australia','Mexico'):
    value = ht.get(key)
    print(value)
# %%
print(ht['Bangladesh'])
# %%
