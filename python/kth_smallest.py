def kth_smallest(k, x):
    if (k > len(x) or k < 1):
        return None
    x.sort()
    return x[k - 1]

def kth_smallest_linear(k, x):
    '''
    Implement a selection algorithm
    '''
    if (k > len(x) or k < 1):
        return None
