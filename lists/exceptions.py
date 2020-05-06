from nodes import SingleListNode
from list import List

class EmptyListException(Exception):
    if not self.head:
        return EmptyListException


class InvalidPositionException(Exception):
    node = self.head
    for position in range(0,self.size-1):
        node = node.next
        if position <0 or position > self.size:
            return InvalidPositionException

class NoSuchElementException(Exception):
    node = self.head
    for i in range(i,self.size-1):
        node = node.next
    if not node:
        return NoSuchElementException
    
