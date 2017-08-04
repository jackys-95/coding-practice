class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return self.items.__str__()

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if self.is_empty is False:
            return self.items[0]

    def is_empty(self):
        return True if self.items > 0 else False
