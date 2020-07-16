#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        #add a specified (default = 8) number of linked list objects.  
        for i in range(init_size):
            #each node of the linked list will contain a tuple in the form of (key,value) as the value for its self/data' attributex
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        # call function items() and iterate through the reslt
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n) where n is the number of key-value pairs in the hash table.  we're a;ways having to go through each bucket (and the linked list nodes they contain) one by one, which totals to n """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            #using the items() method imported from linkedlist.py
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Runnign time is O(n) where n is the number of key-value pairs in the hash table.  we're a;ways having to go through each bucket (and the linked list nodes they contain) one by one, which totals to n"""
        
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) where n is the number of key-value pairs in the hash table.  we're going through each bucket and the linked list nodes they contain, incrementing the count by one at each node.  If we create a self.length 

        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        # each bucket is a linked list
        for bucket in self.buckets:
            #using the items() method imported from linkedlist.py
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time is O(n) where n is the number of key-value pairs in the hash table.  we're always having to go through each bucket (and the linked list nodes they contain) one by one, which totals to n.

        If we create a length attribute for our linked list to store its length, though, our complexity could be the number of buckets instead.
        """
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        count = 0
        for bucket in self.buckets:
            for key, value in bucket.items():
                count = count + 1
        return count

    def contains(self, key_target):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time is O(n) where n is the number of key-value pairs in the hash table.  we're always having to go through each bucket (and the linked list nodes they contain) one by one, which totals to n. 

        If we hash the key_target, we can get to the bucket the key should be in, and therefore we do not need to iterate through every bucket
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        for bucket in self.buckets:
            for key, value in bucket.items():
                if key == key_target:
                    return True
        return False


    def get(self, key_target):
        """Return the value associated with the given key, or raise KeyError.
        TODO:  Running time is O(b) where b is the length of the bucket that the key-value pair belongs to. the hash function obivates the need to iterate through every"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        for bucket in self.buckets:
            for key, value in bucket.items():
                if key == key_target:
                    return value
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time is O(b) where b is the length of the bucket that the key-value pair belongs to. the hash function obivates the need to iterate through every."""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

        bucket_index = hash(key) % len(self.buckets)
        bucket_ll = self.buckets[bucket_index]
        if (self.contains(key) == False):
            bucket_ll.append((key, value))
            #print("value-key pair not yet exists")
        else:
            print("value-key pair exists")
            print("the new  desired value for key is: " + str(value))
            old_value = self.get(key)
            print("existing value is " + str(old_value))
            print("new value is " + str(value))
            bucket_ll.delete((key,old_value))
            bucket_ll.append((key,value))


    def delete(self, key_target):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        
        value_target = None
        pair_exists = False
        for bucket in self.buckets:
            for key,value in bucket.items():
                if key_target == key:
                    value_target = value
                    pair_exists = True
        if pair_exists == False:
            raise KeyError('Key not found: {}'.format(key))
        else :
            bucket_index = hash(key_target) % len(self.buckets)
            bucket_ll = self.buckets[bucket_index]
            bucket_ll.delete((key_target, value_target))

if __name__ == '__main__':
    ht = HashTable()
    ht.set("hi",2)
    ht.set("bye",3)
    ht.set("bros", 4)
    #print (ht.contains('bye'))
    print (ht)
    (ht.set("bye",300))
    print (ht)

    # print(ht.get("bye"))
    # ht.delete("bye")
    #print (ht)
    # print (ht.contains('bye'))

