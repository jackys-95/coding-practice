class SimpleStack:
    '''
    Simple stack implemented with list top of stack is at front of list
    '''
    def __init__(self):
        self.items = []

    def is_empty(self):
        return True if len(self.items) == 0 else False

    def push(self, x):
        self.items = [x] + self.items

    def peek(self):
        return self.items[0]

    def pop(self):
        return self.items.pop(0)
