from exceptions import NoSuchElementException
class Iterator(ABC):
    # Returns true iff the iteration has more elements.
    # In other words, returns true next would return an element rather than throwing an exception.
    def has_next(self):
        if self.has_next:
            return True

    # Returns the next element in the iteration.
    # Throws NoSuchElementException
    def next(self):
        node = self.head
        if self.has_next:
            node = self.has_next
            return node
        elif not self.has_next:
            return NoSuchElementException
        

    # Restarts the iteration. After rewind, if the iteration is not empty, next will return the first element in the iteration.
    def rewind(self): pass

class TwoWayIterator(Iterator):
    # Returns true iff the iteration has more elements in the reverse direction.
    # In other words, returns true if previous would return an element rather than throwing an exception.
    def has_previous(self):
        if self.has_previous:
            return True
    
    # Returns the previous element in the iteration.
    # Throws NoSuchElementException
    def previous(self):
        if self.has_previous:
            result = self.has_previous
            return result
        else:
            return NoSuchElementException

    # Restarts the iteration in the reverse direction. After fullForward, if the iteration is not empty, previous will return the last element in the iteration.
    def full_forward(self): pass
