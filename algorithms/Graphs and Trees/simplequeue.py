class SimpleQueue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return self.items.__str__()

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if self.is_empty() is False:
            return self.items.pop(0)

    def is_empty(self):
        return False if len(self.items) > 0 else True
