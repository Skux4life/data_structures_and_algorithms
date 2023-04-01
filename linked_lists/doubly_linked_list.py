class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head != None:
            self.head.previous = new_node
            self.head = new_node
            new_node.previous = None
        else:
            # If the list is empty then the new node becomes both the head and the tail
            self.head = new_node
            self.tail = new_node
            new_node.previous = None

    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.previous = self.tail

        if self.tail == None:
            # If the list is empty then the new node becomes both the head and the tail
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
    
    def peek_front(self):
        """returns first element"""
        if self.head:
            return self.head.data
        else:
            return None
    
    def peek_back(self):
        """returns last element"""
        if self.tail:
            return self.tail.data
        else:
            return None

    def pop_front(self):
        """removes and returns the first element"""
        if self.head:
            temp = self.head
            temp.next.previous = None # remove previous pointer referring to old head
            self.head = temp.next
            temp.next = None # remove next pointer referring to new head
            return temp.data
        else:
            return None
    
    def pop_back(self):
        """removes and returns the last element"""
        if self.tail:
            temp = self.tail
            temp.previous.next = None # remove previous pointer referring to old tail
            self.tail = temp.previous
            temp.previous = None # remove previous pointer referring to new tail
            return temp.data
        else:
            return None

    def insert_after(self, temp_node, new_data):
        if temp_node:
            new_node = Node(new_data)
            new_node.next = temp_node.next
            temp_node.next = new_node
            new_node.previous = temp_node
            if new_node.next:
                new_node.next.previous = new_node
            if temp_node == self.tail:
                self.tail = new_node
        else:
            return None
    
    def insert_before(self, temp_node, new_data):
        if temp_node:
            new_node = Node(new_data)
            new_node.previous = temp_node.previous
            temp_node.previous = new_node
            new_node.next = temp_node
            if new_node.previous:
                new_node.previous.next = new_node
            if temp_node == self.head:
                self.head = new_node
        else:
            return None
            