# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        hash = self._hash_mod(key)
        keyValue = self.storage[hash]
        if keyValue != None:
            #add it to linked list chain
            while keyValue.next != None:
                if keyValue.key == key:
                    keyValue.value = value
                    return
                keyValue = keyValue.next
            keyValue.next = LinkedPair(key, value)
        else:
             self.storage[hash] = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        keyValue = self.storage[index]
        if index >= 0 and index < self.capacity and keyValue != None:
            prev = None
            while keyValue != None:
                if keyValue.key == key:
                    if prev != None:
                        prev.next = keyValue.next
                    else:
                        self.storage[index] = keyValue
                    return
                prev = keyValue
                keyValue = keyValue.next
            print("Key not found!")
        else:
            print("Key not found!")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if index >= 0 and index < self.capacity and self.storage[index] != None:
            keyValue = self.storage[index]
            while keyValue.key != key:
                keyValue = keyValue.next 
                if keyValue == None:
                    return None
            return keyValue.value
        else: 
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        oldStorage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for i in range(0, self.capacity / 2):
            curr = oldStorage[i]
            while curr != None:
                self.insert(curr.key, curr.value)    


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
