from minheap import MinHeap

class SimplePriorityQueue(MinHeap):
    '''
    Priority queue built with a min-heap
    '''
    def __init__(self, values):
        super().__init__(values)

    def extract_min(self):
        return super().delete_min()

    def decrease_key(self, index, key):
        '''
        Decreases key of heap at index i
        '''
        if (self.array[index] < key):
            raise ValueError("Key is lesser than key at index: " + str(index))

        self.array[index] = key
        while index > 0:
            parent_index = self._find_parent(index)
            if parent_index < 0:
                return
            parent_value = self.array[parent_index]
            self.array[parent_index] = self.array[index]
            self.array[index] =  parent_value
            index = parent_index
