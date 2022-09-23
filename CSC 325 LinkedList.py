class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""
    
    #nested _Node class
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = 'element', '_next'         #streamline memory usage
        
        def __init__(self, element, next):     #initialize node's fields
            self._element = element            #reference to user's element
            self._next = next                  #reference to next node
            
            
    #stack Methods
    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0
        
    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size
    
    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0
    
    def push(self,e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)  #create and link a new node
    
    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element              #top of stack is at head of list
    
    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is Empty')
        answer = self._head._element
        self._head = self._head._next         #bypass the former top node
        self._size -= 1
        return answer

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""
    
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = 'element', '_next'         #streamline memory usage
        
        def __init__(self, element, next):     #initialize node's fields
            self._element = element            #reference to user's element
            self._next = next                  #reference to next node
            
    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0                        #number of queue elements
        
    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
    
    def is_empty(self):
        """Return Ture if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element           #front aligned with head of list
    
    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise EMpty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_emoty():                 #special cas as queue is empty
            self._tail = None               #removed head had been the tail
        return answer
    def enqueue(self,e):
        """Add an element to the back of the queue."""
        newest = self._Node(e, None)        #node will be new tail node
        if self.is_empty():
            self._head = newest             #special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest                 #update reference to tail node
        self._size += 1
        

class _DoublyLinkedBase:
    """A base class providing a doubly linke list representation."""
    
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = 'element', '_next'         #streamline memory usage
        
        def __init__(self, element, next):     #initialize node's fields
            self._element = element            #reference to user's element
            self._next = next                  #reference to next node
            
    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer     #trailer is after header
        self._trailer.prev = self._header      #header is before trailer
        self._size == 0                        #number of elements
        
    def __len__(self):
        """Return the number of elements in the list."""
        return self._size
    
    def is_empty(self):
        """Return True if list is empty"""
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)  #linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        """Delete nosentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                        #record deleted element
        node._prev = node._next = node._element = None #deprecate node
        return element
    
    
    