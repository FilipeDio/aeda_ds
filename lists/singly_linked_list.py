from nodes import SingleListNode
from list import List
from exceptions import EmptyListException
from exceptions import InvalidPositionException
class singly_linked_list(list):

    def _init_(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    # Returns true iff the list contains no elements.
    def is_empty(self): 
        if not self.head:
            return True

    # Returns the number of elements in the list.
    def size(self):
        return self.num_elements

    # Returns the first element of the list.
    # Throws EmptyListException
    def get_first(self):
        if self.head:
            return self.head
        else:
            return EmptyListException

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        if self.head:
            return self.tail
        else:
            return EmptyListException

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        node = self.head
        for position in range(0,self.size-1):
            node= node.next
        if position:
            return position.data


    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list
    def find(self, element):
        node = self.head
        for i in range (i,self.size-1):
            node = node.next
        if node:
            node.data = element
            return node.data
        else:
            return -1

            



    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        self.head.insert_first(element)
        self.num_elements=+1

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        self.tail.insert_last(element)
        self.num_elements=+1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        node = self.head
        for position in range (0,self.size-1):
            node = node.get_next()
        if position <0 and position > self.size:
            node.insert(element) 
        elif position == 0:
            self.head.insert_first(element)
            return self.head
        elif position == self.size:
            self.tail.insert_last(element)
            return self.tail
        else:
            return InvalidPositionException
        self.num_elements=+1



    
    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException
    def remove_first(self): 
        if self.head:
            self.head.remove
            self.num_elements=-1
            return self.head
        elif not self.head:
            return EmptyListException
        self.num_elements=-1

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        if self.tail:
            self.tail.remove
            self.num_elements=-1
            return self.tail
        elif not self.tail:
            return EmptyListException
        self.num_elements =-1
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException
    def remove(self, position):
        node = self.head
        for position in range (0,self.size-1):
            node = node.next
        if position:
            node.remove
        else:
            return InvalidPositionException
        self.num_elements =-1
    # Removes all elements from the list.
    def make_empty(self):
        if self.head:
            return not self.head

    # Returns an iterator of the elements in the list (in proper sequence)
    def iterator(self): pass
