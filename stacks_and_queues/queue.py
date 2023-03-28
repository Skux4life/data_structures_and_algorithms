class Queue:
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item):
        self.items.append[item]

    def dequeue(self):
        item = self.read()
        self.items.remove(0)
        return item
    
    def read(self):
        return self.items[0]