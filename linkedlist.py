  
#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                #print ("this is " + item)
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            print("the item is " + item)
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
            #print(node)
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None



    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time:  length() iterates through each node of the linked list, updating the count at each node, which means the complexity is O(n), where n is the length of the linked list.  This is true under all conditions ( a possible exception is when the linked list is empty, the case in which the complexity is 0(1)). 
        """
        count = 0
        temp = self.head
        while temp != None:
            count = count + 1
            temp = temp.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) because we simply need to change the head and tail node or hcnage the tail node and its next node. The size of the linkedin list is irrelevant"""
        
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # print ("node being appended is ") 
        # print(new_node)

        # TODO: If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty() == True:
            # print("linked list is empty...so let's assign new head and tail values")
            self.head = new_node
            self.tail = new_node
            # print (self.head)
            # print (self.tail)
            # print ("++++++++++++++++++++++")

        # TODO: Else append node after tail
        else:
            # print("linked list is NOT empty....")
            self.tail.next = new_node
            # print ("self.tail.next is updated to ")
            # print (self.tail.next)
            self.tail = new_node
            # print ("self.tail is updated to ") 
            # print (self.tail)
            # print ("++++++++++++++++++++++")

        #print (self.head)
        #print (self.tail)

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Under any circumstances, we're are merely changing the head and/or tail node value.  These are constant time oeprations"""
        
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists
        new_node.next = self.head
        self.head = new_node

        if self.tail == None:
            self.tail = new_node

    def find(self, item):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: the head node is what we are looking for, so we need only 1 iteration and the  complexity is O(1) 
        TODO: Worst case running time: length() iterates through each node of the linked list and did not find a match, meaning the complexity is O(n)"""
        # TODO: Loop through all nodes to find item, if present return True otherwise False
        node = self.head
        while node != None:
            if node.data == item:
                return True
            node = node.next
        return False


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        #case 1: linked list is empty
        if self.head == None and self.tail == None:
            return ValueError('Item not found: {}'.format(item))

        #case 2: only one node exist, which is both tail and head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return item
       
        # the case of deleting self.head
        if item == self.head.data:
            self.head = self.head.next
            return item

        #case 4: the usual case with head and tail non-null
        previous = self.head
        current = self.head.next

        while current != None:
            if current.data == item:
                if current == self.tail:
                    self.tail = previous
                previous.next = current.next 
                return item
            previous = current
            current = current.next

        return ValueError('Item not found: {}'.format(item))
        


if __name__ == "__main__":
    my_ll = LinkedList(["A", "B", "C"])
    print(my_ll)



