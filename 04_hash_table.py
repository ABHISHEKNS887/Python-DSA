# Hash Tables in Data Structures and Algorithms (DSA)
# A hash table (or hash map) is a data structure that provides fast insertion, deletion, and lookup operations. 
# It stores key-value pairs and uses a hash function to compute an index (or hash code) to store values efficiently.

# Key Concepts
# Hash Function:

# Converts a key into an index in the array.
# A good hash function ensures uniform distribution of keys to minimize collisions.
# Collision Handling Techniques:

# Chaining (Separate Chaining): Uses linked lists to store multiple values at the same index.
# Open Addressing:
# Linear Probing: Searches for the next available slot in a sequential manner.
# Quadratic Probing: Uses a quadratic function to find the next available slot.
# Double Hashing: Uses a second hash function to resolve collisions.
# Load Factor:

# Defined as (number of elements) / (size of hash table).
# If the load factor becomes too high, the table is resized (typically doubled in size).
# Operations:

# Insertion: Compute hash index using the hash function and store the key-value pair.
# Deletion: Locate the key using the hash function and remove it.
# Search (Lookup): Compute the hash index and retrieve the corresponding value.
# Time Complexity
# Operation	Average Case	Worst Case
# Insert	O(1)	O(n) (if collisions are high)
# Search	O(1)	O(n)
# Delete	O(1)	O(n)
# With good hash functions and load factor management, operations are close to O(1) in most cases.

# Implementation in Python

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Using separate chaining
    
    def _hash_function(self, key):
        return hash(key) % self.size  # Simple hash function
    
    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update existing key
                return
        self.table[index].append([key, value])  # Insert new key-value pair
    
    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found
    
    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False  # Key not found

# Example usage:
ht = HashTable()
ht.insert("name", "Abhishek")
ht.insert("age", 25)
print(ht.get("name"))  # Output: Abhishek
ht.delete("age")
print(ht.get("age"))  # Output: None

# Use Cases of Hash Tables
# Database Indexing
# Caching Mechanisms (e.g., LRU Cache)
# Symbol Tables in Compilers
# Counting Frequencies (e.g., word count)
# Implementing Sets (Python set is internally a hash table)

# ---------------------------------------------------------------------------------------------------------------------------

class HashTable:
    
    def __init__(self, size=7):
        self.data_map = [None] * size
        
    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
            
    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        
    def get_item(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
        
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
                
    
my_hash_table = HashTable()
my_hash_table.set_item('bolt', 1400)
my_hash_table.set_item('washer', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()
print(my_hash_table.get_item('bolt'))
print(my_hash_table.keys())