class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()
    
    def read(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0