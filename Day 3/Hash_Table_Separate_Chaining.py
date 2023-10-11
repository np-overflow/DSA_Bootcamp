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
            self.table[index] = []

        ## Append the (key, value) tuple to the list
        self.table[index].append((key, value))

    ## Remove Function
    def remove(self, key):
        ## Get the index from the hash function
        index = self.hash_function(key)

        ## If the index is empty, raise KeyError
        ## KeyError is a Python exception thrown when a key is not found.
        if self.table[index] is None:
            raise KeyError(key)
        
        ## Loop through the list to find the key
        for i in range(len(self.table[index])):
            ## If the key is found, remove the (key, value) tuple
            if self.table[index][i][0] == key:
                self.table[index].pop(i)
                return
        
        ## If the key is not found, raise KeyError
        raise KeyError(key)
    
    ## Get Function
    def get(self, key):
        ## Get the index from the hash function
        index = self.hash_function(key)

        ## If the index is empty, raise KeyError
        if self.table[index] is None:
            raise KeyError(key)
        
        ## Loop through the list to find the key
        for i in range(len(self.table[index])):
            ## If the key is found, return the value
            if self.table[index][i][0] == key:
                return self.table[index][i][1]
        
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
                for tuple in range(len(self.table[index])):
                    ## Append the (key, value) tuple to the string
                    string += str(self.table[index][tuple]) + " "
        
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
