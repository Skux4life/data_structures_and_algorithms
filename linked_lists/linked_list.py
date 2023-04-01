class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
        nodes.append("None")
        return "->".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def read(self, index):
        current_node = self.head
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            current_index += 1
        
        return current_node if current_node else None

    def index_of(self, value):
        current_index = 0
        for node in self:
            if node.data == value:
                return current_index
            else:
                current_index += 1
        return None


    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head == None:
            raise Exception("List is empty")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        
        raise Exception(f'Node with data "{target_node_data} not found')
    
    def insert_at_index(self, index, value):
        new_node = Node(value)

        if index == 0:
            self.add_first(new_node)
            return
        
        current_node = self.head
        current_index = 0

        while current_index < index - 1:
            current_node = current_node.next
            current_index += 1
        
        new_node.next = current_node.next
        current_node.next = new_node
        return

    def delete_at_index(self, index):
        if index == 0:
            self.head = self.head.next
            return
        
        current_node = self.head
        current_index = 0

        while current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        node_after_deleted_node = current_node.next.next
        current_node.next = node_after_deleted_node
        return

