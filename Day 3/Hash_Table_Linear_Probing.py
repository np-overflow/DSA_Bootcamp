class HashTable:
    ## Constructor
    def __init__(self, size):
        ## Size of the Hash Table.
        self.size = size

        ## Initial Table with None Object.
        self.table = [None] * size

    ## Hash Function
    def hash_function(self, key):
        ## hash() is a built-in Python function that returns a hash value.
        ## The hash value is a unique integer that represents the input data (strings/numbers)
        return hash(key) % self.size
    
    ## Insert Function
    def insert(self, key, value):
        ## Get the index from the hash function
        index = self.hash_function(key)

        ## If the index is empty, create a new list
        if self.table[index] is None:
            ## NOTE: Instead of new empty list, points to tuple
            self.table[index] = (key, value)
        else:
            ## Linear probing: searching for the next available slot
            next_index = (index + 1) % self.size
            while next_index != index:
                if self.table[next_index] is None:
                    self.table[next_index] = (key, value)
                    return
                next_index = (next_index + 1) % self.size
            ## If the table is full, raise Exception
            raise Exception("Hash Table is full")

    ## Remove Function
    def remove(self, key):
        ## Get the index from the hash function
        index = self.hash_function(key)
        start_index = index

        ## Looping through the table to find the key
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size

            ## If index is back to the start index, break out of loop
            if(index == start_index):
                break
        
        ## If the key is not found, raise KeyError
        raise KeyError(key)
    
    ## Get Function
    def get(self, key):
        ## Get the index from the hash function
        index = self.hash_function(key)
        start_index = index

        ## Looping through the table to find the key
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size

            ## If index is back to the start index, break out of loop
            if(index == start_index):
                break
        
        ## If the key is not found, raise KeyError
        raise KeyError(key)
    
    ## Print Function
    def __str__ (self):
        ## String to be returned
        string = ""

        ## Loop through the table
        for index in range(self.size):
            ## If the index is not empty, loop through the list
            if self.table[index] is not None:
                string += str(self.table[index]) + " "
        
        ## Return the string
        return string

hash_table = HashTable(10)
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("cherry", 30)

print(hash_table.get("apple")) # Output: 10
print(hash_table)

hash_table.remove("banana")
print(hash_table)
