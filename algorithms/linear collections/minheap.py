class MinHeap:
    '''
    Array implementation of min-heap
    '''
    def __init__(self, values):
        self.array = values
        self.current_size = len(values)
        for i in range(((self.current_size // 2) - 1), -1, -1):
            self._heapify(self.array, i)

    def is_empty(self):
        return True if len(self.array) == 0 else False

    def insert(self, item):
        '''
        Inserts item into the heap
        '''
        self.array.append(item)
        index = len(self.array)

        while index > 0:
            parent_index = self._find_parent(index)
            if parent_index < 0:
                return
            parent_value = self.array[parent_index]
            self.array[parent_index] = item
            self.array[index] =  parent_value
            index = parent_index

    def find_min(self):
        return self.array[0]

    def delete_min(self):
        return

    def _heapify(self, values, index):
        '''
        Builds heap out of list of integers
        Assume left and right subtrees at index are min-heaps
        '''
        left = self._find_left_child(index)
        right = self._find_right_child(index)
        index_of_smallest = 0
        smallest_value = 0

        if (left < self.current_size and self.array[left] < self.array[index]):
            index_of_smallest = left
            smallest_value = self.array[left]
        else:
            index_of_smallest = index
            smallest_value = self.array[index]
        if (right < self.current_size and self.array[right] < self.array[index_of_smallest]):
            index_of_smallest = right
            smallest_value = self.array[right]
        if (index_of_smallest != index):
            self.array[index_of_smallest] = self.array[index]
            self.array[index] = smallest_value
            self._heapify(self.array, index_of_smallest)

    def _find_parent(self, index):
        '''
        Finds parent index
        '''
        return ((index + 1) // 2) - 1

    def _find_left_child(self, index):
        '''
        Finds left child index
        '''
        return (2 * (index +  1)) - 1

    def _find_right_child(self, index):
        '''
        Finds right child index
        '''
        return (2 * (index + 1) + 1) - 1

    def __str__(self):
        return str(self.array)

x = MinHeap([10, 11, 4, 5, 2, 3, 9])
print(x)

