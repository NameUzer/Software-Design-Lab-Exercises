# Link list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
# Function to find the second last
# node of the linked list
def findSecondLastNode(head):
    temp = head
    # If the list is empty or
    # contains less than 2 nodes
    if (temp == None or temp.next == None):
        return -1
    # Traverse the linked list
    while (temp != None):
        # Check if the current node is the
        # second last node or not
        if (temp.next.next == None):
            return temp.data     
        # If not then move to the next node
        temp = temp.next
# Function to push node at head
def push(head, new_data):
    new_node = Node(new_data)
    #new_node.data = new_data
    new_node.next = head
    head = new_node
    return head
# Driver code
if __name__ == '__main__':
    # Start with the empty list
    head = None
    # Use push() function to construct
    # the below list 8 . 23 . 11 . 29 . 12
    head = push(head, 12)
    head = push(head, 29)
    head = push(head, 11)
    head = push(head, 23)
    head = push(head, 8)
 
    print(findSecondLastNode(head))

import copy
class Empty(Exception):
    pass
class LinkedStack:
    """LIFO Stack implementatino using a singly linked list for storage"""
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt
    def __init__(self):
        self._head = None
        self._size = 0    
    def __len__(self):
        return self._size
    def __iter__(self):
        cur = self._head
        while cur is not None:
            yield cur._element
            cur = cur._next 
    def is_empty(self):
        return self._size == 0
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
L = LinkedStack()
L.push(5)
L.push(4)
L.push(3)
[i for i in L]
M = LinkedStack()
M.push(3)
M.push(2)
M.push(1)
[i for i in M]
def concat_singly_linked_stack(base, append):
     
    base = copy.deepcopy(base)
    append = copy.deepcopy(append)
    
    base_last = None
    cur = base._head
    while True:  # Need to traverse whole list since LinkedStack does not keep its last node.
        if cur._next is None:
            base_last = cur
            break
        cur = cur._next
    base_last._next = append._head
    base._size += append._size
    return base
concat_list = concat_singly_linked_stack(L, M)
[i for i in concat_list]
